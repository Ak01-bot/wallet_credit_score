import pandas as pd
from load_and_flatten import load_normalized_data
from feature_engineering import extract_features, calculate_heuristic_score
from scoring_model import train_model, predict_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

def main():
    os.makedirs("outputs", exist_ok=True)

    # Step 1: Load data
    df = load_normalized_data("../data/user-wallet-transactions.json")

    # Step 2: Feature extraction
    features = extract_features(df)

    # Step 3: Generate heuristic score (training label)
    features = calculate_heuristic_score(features)

    # Step 4: Train ML model using features and heuristic labels
    X = features.drop(columns=["wallet", "credit_score"])
    y = features["credit_score"]
    model = train_model(X, y)

    # Step 5: Predict score using ML model
    features["ml_credit_score"] = predict_score(model, X)

    # Step 6: Save to CSV
    features[["wallet", "ml_credit_score"]].to_csv("outputs/wallet_scores_ml.csv", index=False)

    # Step 7: Plot distribution
    sns.histplot(features["ml_credit_score"], bins=10, kde=True)
    plt.title("Predicted Wallet Credit Score Distribution")
    plt.xlabel("Credit Score")
    plt.ylabel("Number of Wallets")
    plt.savefig("outputs/score_distribution.png")

    print(" ML scoring complete. Outputs saved.")

if __name__ == "__main__":
    main()
