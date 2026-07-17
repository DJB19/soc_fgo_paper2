#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <cmath>

#include <gtsam/nonlinear/NonlinearFactorGraph.h>
#include <gtsam/nonlinear/LevenbergMarquardtOptimizer.h>
#include <gtsam/nonlinear/Values.h>
#include <gtsam/inference/Symbol.h>
#include <gtsam/slam/PriorFactor.h>

#include "SOCProcessFactor.h"
#include "SOCVoltageFactorNonlinear.h"

using namespace std;
using namespace gtsam;

int main(int argc, char* argv[]) {

    if (argc != 3) {
        cerr << "Usage: " << argv[0]
             << " <input_csv> <output_csv>" << endl;
        return 1;
    }

    const string input_file = argv[1];
    const string output_file = argv[2];

    ifstream file(input_file);

    if (!file.is_open()) {
        cerr << "Cannot open file: "
             << input_file << endl;
        return 1;
    }

    vector<double> time;
    vector<double> current;
    vector<double> voltage;
    vector<double> soc_true;

    string line;
    getline(file, line);

    while (getline(file, line)) {
        stringstream ss(line);
        string item;
        vector<double> row;

        while (getline(ss, item, ',')) {
            row.push_back(stod(item));
        }

        if (row.size() >= 4) {
            time.push_back(row[0]);
            current.push_back(row[1]);
            voltage.push_back(row[2]);
            soc_true.push_back(row[3]);
        }
    }

    file.close();

    const size_t N = time.size();

    if (N < 2) {
        cerr << "Insufficient data in: "
             << input_file << endl;
        return 1;
    }

    cout << "Input: " << input_file << endl;
    cout << "Data length: " << N << endl;

    const double capacity_Ah = 3.0;

    const double R0 = 0.05;
    const double R1 = 0.02;
    const double C1 = 2000.0;

    /*
     * Coulomb-counting initial estimate.
     *
     * Each current sample in the generated CSV corresponds
     * to the SOC and voltage stored in the same row.
     * Therefore, transition k-1 -> k uses current[k].
     */
    vector<double> soc_cc(N);
    soc_cc[0] = soc_true[0];

    for (size_t k = 1; k < N; ++k) {

        double dt = time[k] - time[k - 1];

        soc_cc[k] =
            soc_cc[k - 1]
            - current[k] * dt
            / (capacity_Ah * 3600.0);

        if (soc_cc[k] > 1.0) {
            soc_cc[k] = 1.0;
        }

        if (soc_cc[k] < 0.0) {
            soc_cc[k] = 0.0;
        }
    }

    /*
     * Polarization-voltage reconstruction using the
     * first-order RC model and measured current.
     */
    vector<double> v_rc(N, 0.0);

    double dt0 = time[1] - time[0];
    double alpha0 = exp(-dt0 / (R1 * C1));

    v_rc[0] =
        (1.0 - alpha0)
        * R1
        * current[0];

    for (size_t k = 1; k < N; ++k) {

        double dt = time[k] - time[k - 1];
        double alpha = exp(-dt / (R1 * C1));

        v_rc[k] =
            alpha * v_rc[k - 1]
            + (1.0 - alpha)
            * R1
            * current[k];
    }

    NonlinearFactorGraph graph;
    Values initial;

    auto priorNoise =
        noiseModel::Isotropic::Sigma(1, 1e-4);

    auto processNoise =
        noiseModel::Isotropic::Sigma(1, 1e-3);

    auto voltageNoise =
        noiseModel::Isotropic::Sigma(1, 0.02);

    for (size_t k = 0; k < N; ++k) {
        initial.insert(
            Symbol('x', k),
            soc_cc[k]
        );
    }

    graph.add(
        PriorFactor<double>(
            Symbol('x', 0),
            soc_true[0],
            priorNoise
        )
    );

    /*
     * SOC transition factors.
     * SOCProcessFactor uses a plus sign internally,
     * so negative current is passed for discharge.
     */
    for (size_t k = 0; k < N - 1; ++k) {

        double dt = time[k + 1] - time[k];

        graph.emplace_shared<SOCProcessFactor>(
            Symbol('x', k),
            Symbol('x', k + 1),
            -current[k + 1],
            dt,
            capacity_Ah,
            processNoise
        );
    }

    /*
     * Nonlinear terminal-voltage factors:
     *
     * V = OCV(SOC) - I*R0 - V_rc
     */
    for (size_t k = 0; k < N; ++k) {

        graph.emplace_shared<SOCVoltageFactorNonlinear>(
            Symbol('x', k),
            voltage[k],
            current[k],
            R0,
            v_rc[k],
            voltageNoise
        );
    }

    LevenbergMarquardtOptimizer optimizer(
        graph,
        initial
    );

    Values result = optimizer.optimize();

    ofstream out(output_file);

    if (!out.is_open()) {
        cerr << "Cannot create output file: "
             << output_file << endl;
        return 1;
    }

    out << "time,soc_true,soc_kf,soc_fgo\n";

    for (size_t k = 0; k < N; ++k) {

        double soc_fgo =
            result.at<double>(Symbol('x', k));

        if (soc_fgo > 1.0) {
            soc_fgo = 1.0;
        }

        if (soc_fgo < 0.0) {
            soc_fgo = 0.0;
        }

        out << time[k] << ","
            << soc_true[k] << ","
            << soc_cc[k] << ","
            << soc_fgo << "\n";
    }

    out.close();

    cout << "Nonlinear FGO estimation completed."
         << endl;

    cout << "Output: "
         << output_file << endl;

    return 0;
}
