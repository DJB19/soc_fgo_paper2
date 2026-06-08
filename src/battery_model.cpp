#include <iostream>
#include <fstream>
#include <cmath>
#include <random>

double ocv(double soc) {
    return 3.0 + 1.2 * soc - 0.1 * std::sin(6.28318 * soc);
}

int main() {
    const double dt = 1.0;
    const int total_time = 12000;
    const double capacity_Ah = 3.0;
    const double Q = capacity_Ah * 3600.0;

    const double R0 = 0.05;
    const double R1 = 0.02;
    const double C1 = 2000.0;

    double soc = 0.8;
    double v_rc = 0.0;

    std::default_random_engine gen(42);
    std::normal_distribution<double> voltage_noise(0.0, 0.10);
    std::uniform_real_distribution<double> current_dist(0.2, 1.0);

    std::ofstream file("sensor_data_random_12000s.csv");
    file << "time,current,voltage,soc_true\n";

    for (int t = 0; t <= total_time; ++t) {
        double I = current_dist(gen);

        soc -= (I * dt) / Q;
        if (soc > 1.0) soc = 1.0;
        if (soc < 0.0) soc = 0.0;

        double alpha = std::exp(-dt / (R1 * C1));
        v_rc = alpha * v_rc + (1.0 - alpha) * R1 * I;

        double V = ocv(soc) - I * R0 - v_rc;
        double V_measured = V + voltage_noise(gen);

        file << t << ","
             << I << ","
             << V_measured << ","
             << soc << "\n";
    }

    file.close();

    std::cout << "Random current battery simulation completed.\n";
    std::cout << "Output: sensor_data_random_12000s.csv\n";

    return 0;
}
