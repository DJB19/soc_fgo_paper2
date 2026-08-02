#ifndef SOC_PROCESS_FACTOR_H
#define SOC_PROCESS_FACTOR_H

#include <gtsam/nonlinear/NonlinearFactor.h>

using namespace gtsam;

class SOCProcessFactor : public NoiseModelFactorN<double, double> {

private:
    double I_;
    double dt_;
    double Q_;

public:
    SOCProcessFactor(Key key1, Key key2, double I, double dt, double Q,
                     const SharedNoiseModel& model)
        : NoiseModelFactorN<double, double>(model, key1, key2),
          I_(I), dt_(dt), Q_(Q) {}

    Vector evaluateError(const double& soc_t, const double& soc_tp1,
                         OptionalMatrixType H1,
                         OptionalMatrixType H2) const override {

        double predicted = soc_t + (I_ * dt_) / (Q_ * 3600.0);
        double error = soc_tp1 - predicted;

        if (H1) *H1 = (Matrix(1,1) << -1.0).finished();
        if (H2) *H2 = (Matrix(1,1) << 1.0).finished();

        return (Vector(1) << error).finished();
    }
};

#endif
