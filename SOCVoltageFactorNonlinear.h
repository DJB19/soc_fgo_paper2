#ifndef SOC_VOLTAGE_FACTOR_NONLINEAR_H
#define SOC_VOLTAGE_FACTOR_NONLINEAR_H

#include <cmath>
#include <gtsam/nonlinear/NonlinearFactor.h>

using namespace gtsam;

class SOCVoltageFactorNonlinear : public NoiseModelFactorN<double> {
private:
    double V_meas_;
    double I_;
    double R_;

public:
    SOCVoltageFactorNonlinear(Key key, double V_meas, double I, double R,
                              const SharedNoiseModel& model)
        : NoiseModelFactorN<double>(model, key),
          V_meas_(V_meas), I_(I), R_(R) {}

    double ocv(double soc) const {
        return 3.0 + 1.2 * soc - 0.1 * std::sin(6.28318 * soc);
    }

    double docv_dsoc(double soc) const {
        return 1.2 - 0.1 * 6.28318 * std::cos(6.28318 * soc);
    }

    Vector evaluateError(const double& soc,
                         OptionalMatrixType H) const override {
        double V_pred = ocv(soc) - R_ * I_;
        double error = V_meas_ - V_pred;

        if (H) *H = (Matrix(1,1) << -docv_dsoc(soc)).finished();

        return (Vector(1) << error).finished();
    }
};

#endif
