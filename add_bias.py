import pandas as pd

df = pd.read_csv("data/paper2_clean_base.csv")

for bias,name in [
    (0.005,"005"),
    (0.01,"010"),
    (0.02,"020"),
    (0.05,"050"),
    (0.10,"100")
]:
    out=df.copy()

    out["current"]=out["current"]*(1+bias)

    out.to_csv(
        f"data/paper2_bias{name}.csv",
        index=False
    )

print("Done")
