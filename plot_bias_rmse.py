import matplotlib.pyplot as plt

bias=[0.5,1,2,5,10]

cc=[0.001912,
    0.003823,
    0.007644,
    0.019107,
    0.038212]

fgo=[0.008784,
     0.008672,
     0.008447,
     0.007775,
     0.006657]

plt.figure(figsize=(8,5))

plt.plot(bias,cc,'o-',label='Coulomb Counting')
plt.plot(bias,fgo,'s-',label='Nonlinear FGO')

plt.xlabel('Current Sensor Bias (%)')
plt.ylabel('RMSE')
plt.grid(True)
plt.legend()

plt.savefig('paper2_bias_rmse.png',dpi=300)
plt.show()
