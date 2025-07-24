from src.load_and_flatten import load_normalized_data

df = load_normalized_data("data/sample_transactions.json")
print(df.head())
print(df.info())
print(df["action"].value_counts())
