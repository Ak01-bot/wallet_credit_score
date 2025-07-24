import pandas as pd

def extract_features(df):
    grouped = df.groupby("wallet").agg({
        "action": [
            lambda x: (x == "deposit").sum(),
            lambda x: (x == "borrow").sum(),
            lambda x: (x == "repay").sum(),
            lambda x: (x == "redeemunderlying").sum(),
            lambda x: (x == "liquidationcall").sum(),
            "count"
        ],
        "token": ["nunique"],
        "timestamp": lambda x: (x.max() - x.min()).days + 1
    })

    grouped.columns = [
        "num_deposits", "num_borrows", "num_repays", "num_redeems", "num_liquidations",
        "total_tx", "token_diversity", "active_days"
    ]
    grouped.reset_index(inplace=True)
    return grouped

def calculate_heuristic_score(df):
    score = (
        200
        + df["num_deposits"] * 10
        + df["num_repays"] * 20
        + df["active_days"] * 1
        - df["num_borrows"] * 5
        - df["num_liquidations"] * 100
    )
    df["credit_score"] = score.clip(0, 1000)
    return df
