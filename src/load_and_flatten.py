import pandas as pd
import json

def load_normalized_data(filepath: str) -> pd.DataFrame:
    with open(filepath, 'r') as f:
        raw_data = json.load(f)

    df = pd.json_normalize(raw_data)

    df.rename(columns={
        "userWallet": "wallet",
        "timestamp": "timestamp",
        "action": "action",
        "actionData.assetSymbol": "token",
        "actionData.amount": "amount",
    }, inplace=True)

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit='s')
    df["amount"] = pd.to_numeric(df["amount"], errors='coerce')
    df = df[["wallet", "action", "token", "amount", "timestamp"]]

    return df
