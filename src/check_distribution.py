import pandas as pd

df = pd.read_csv("E:\wallet_credit_score\src\outputs\wallet_scores_ml.csv")

bins = [0, 100, 200, 400, 700, 900, 1000]
labels = ["0–100", "100–200", "200–400", "400–700", "700–900", "900–1000"]
df["range"] = pd.cut(df["ml_credit_score"], bins=bins, labels=labels, include_lowest=True)

print(df["range"].value_counts().sort_index())
