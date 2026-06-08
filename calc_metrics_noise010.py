import csv, math

files = [
("Noise010 Linear Voltage FGO",
 "results/result_random_linear_voltage_noise010.csv"),

("Noise010 Nonlinear Voltage FGO",
 "results/result_random_nonlinear_voltage_noise010.csv")
]

print("Method,RMSE_FGO")

for name,path in files:

    t=[]
    g=[]

    with open(path) as f:
        r=csv.DictReader(f)

        for row in r:
            t.append(float(row["soc_true"]))
            g.append(float(row["soc_fgo"]))

    rmse=math.sqrt(
        sum((a-b)**2 for a,b in zip(t,g))/len(t)
    )

    print(name,rmse)
