#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>

#include <gtsam/nonlinear/NonlinearFactorGraph.h>
#include <gtsam/nonlinear/LevenbergMarquardtOptimizer.h>
#include <gtsam/nonlinear/Values.h>
#include <gtsam/inference/Symbol.h>
#include <gtsam/slam/PriorFactor.h>

#include "SOCProcessFactor.h"
#include "SOCVoltageFactorNonlinear.h"

using namespace std;
using namespace gtsam;

int main() {
    const string input_file = "data/sensor_data_12000s.csv";
    const string output_file = "results/result_case1_nonlinear_voltage_fgo.csv";

    ifstream file(input_file);
    if (!file.is_open()) {
        cerr << "Cannot open file: " << input_file << endl;
        return 1;
    }

    vector<double> time, current, voltage, soc_true;
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

    size_t N = time.size();
    cout << "Data length: " << N << endl;

    const double dt = 1.0;
    const double capacity_Ah = 3.0;
    const double R0 = 0.05;

    vector<double> soc_kf(N);
    soc_kf[0] = soc_true[0];

    for (size_t i = 1; i < N; ++i) {
        soc_kf[i] = soc_kf[i - 1] - current[i - 1] * dt / (capacity_Ah * 3600.0);
        if (soc_kf[i] > 1.0) soc_kf[i] = 1.0;
        if (soc_kf[i] < 0.0) soc_kf[i] = 0.0;
    }

    NonlinearFactorGraph graph;
    Values initial;

    auto priorNoise = noiseModel::Isotropic::Sigma(1, 1e-4);
    auto processNoise = noiseModel::Isotropic::Sigma(1, 1e-3);
    auto voltageNoise = noiseModel::Isotropic::Sigma(1, 0.02);

    for (size_t i = 0; i < N; ++i) {
        initial.insert(Symbol('x', i), soc_kf[i]);
    }

    graph.add(PriorFactor<double>(Symbol('x', 0), soc_true[0], priorNoise));

    for (size_t i = 0; i < N - 1; ++i) {
        graph.emplace_shared<SOCProcessFactor>(
            Symbol('x', i),
            Symbol('x', i + 1),
            -current[i],
            dt,
            capacity_Ah,
            processNoise
        );
    }

    for (size_t i = 0; i < N; ++i) {
        graph.emplace_shared<SOCVoltageFactorNonlinear>(
            Symbol('x', i),
            voltage[i],
            current[i],
            R0,
            voltageNoise
        );
    }

    LevenbergMarquardtOptimizer optimizer(graph, initial);
    Values result = optimizer.optimize();

    ofstream out(output_file);
    out << "time,soc_true,soc_kf,soc_fgo\n";

    for (size_t i = 0; i < N; ++i) {
        double soc_fgo = result.at<double>(Symbol('x', i));

        if (soc_fgo > 1.0) soc_fgo = 1.0;
        if (soc_fgo < 0.0) soc_fgo = 0.0;

        out << time[i] << ","
            << soc_true[i] << ","
            << soc_kf[i] << ","
            << soc_fgo << "\n";
    }

    out.close();

    cout << "Nonlinear voltage FGO estimation DONE!" << endl;
    cout << "Output: " << output_file << endl;

    return 0;
}
