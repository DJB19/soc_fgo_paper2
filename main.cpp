make -j8#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>



#include <memory>

#include <gtsam/nonlinear/NonlinearFactorGraph.h>
#include <gtsam/nonlinear/LevenbergMarquardtOptimizer.h>
#include <gtsam/nonlinear/PriorFactor.h>
#include <gtsam/nonlinear/Values.h>
#include <gtsam/inference/Symbol.h>

#include "SOCProcessFactor.h"

using namespace std;
using namespace gtsam;

int main() {
    string filename = "sensor_data_12000s.csv";

    vector<double> time, voltage, current, soc_true, soc_kf;

    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Cannot open file: " << filename << endl;
        return 1;
    }

    string line;
    getline(file, line); // skip header

    while (getline(file, line)) {
        stringstream ss(line);
        string value;
        vector<double> row;

        while (getline(ss, value, ',')) {
            if (!value.empty()) {
                row.push_back(stod(value));
            }
        }

        if (row.size() >= 5) {
            time.push_back(row[0]);
            voltage.push_back(row[1]);
            current.push_back(row[2]);
            soc_true.push_back(row[3]);
            soc_kf.push_back(row[4]);
        }
    }

    size_t N = current.size();
    cout << "Data length: " << N << endl;

    NonlinearFactorGraph graph;
    Values initial;

    const double Q = 11.4346;  // Ah, from MATLAB workspace AH = 27

    auto priorNoise   = noiseModel::Isotropic::Sigma(1, 0.001);
    auto processNoise = noiseModel::Isotropic::Sigma(1, 0.01);

    double initialSOC = soc_true[0];

    initial.insert(Symbol('x', 0), initialSOC);
    graph.add(PriorFactor<double>(Symbol('x', 0), initialSOC, priorNoise));

    for (size_t t = 0; t < N - 1; ++t) {
        double dt = time[t + 1] - time[t];
        if (dt <= 0) {
            dt = 1.0;
        }

        Symbol key1('x', t);
        Symbol key2('x', t + 1);

        initial.insert(key2, soc_kf[t + 1]);

        graph.add(std::make_shared<SOCProcessFactor>(
            key1, key2, current[t], dt, Q, processNoise
        ));
    }

    LevenbergMarquardtOptimizer optimizer(graph, initial);
    Values result = optimizer.optimize();

    ofstream out("estimated_SOC_fgo_sensor_data_12000s.csv");
    out << "time,SOC_true,SOC_kf,SOC_fgo\n";

    for (size_t t = 0; t < N; ++t) {
        double soc_fgo = result.at<double>(Symbol('x', t));
        out << time[t] << ","
            << soc_true[t] << ","
            << soc_kf[t] << ","
            << soc_fgo << "\n";
    }

    cout << "Current-only FGO DONE!" << endl;
    cout << "Output: estimated_SOC_fgo_sensor_data_12000s.csv" << endl;

    return 0;
}
