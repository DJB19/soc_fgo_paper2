#ifndef SOC_VOLTAGE_FACTOR_H
#define SOC_VOLTAGE_FACTOR_H

#include <gtsam/nonlinear/NonlinearFactor.h>

using namespace gtsam;

class SOCVoltageFactor : public NoiseModelFactorN<double> {

private:
    double V_meas_;
    double I_;
    double ocv0_;
    double ocv_slope_;
    double R_;

public:
    SOCVoltageFactor(Key key, double V_meas, double I,
                     double ocv0, double ocv_slope, double R,
                     const SharedNoiseModel& model)
        : NoiseModelFactorN<double>(model, key),
          V_meas_(V_meas), I_(I),
          ocv0_(ocv0), ocv_slope_(ocv_slope), R_(R) {}

    Vector evaluateError(const double& soc,
                         OptionalMatrixType H) const override {

        double V_pred = ocv0_ + ocv_slope_ * soc - R_ * I_;
        double error = V_meas_ - V_pred;

        if (H) *H = (Matrix(1,1) << -ocv_slope_).finished();

        return (Vector(1) << error).finished();
    }
};

#endif
