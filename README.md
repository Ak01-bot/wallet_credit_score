# DeFi Wallet Credit Scoring - Aave V2 Protocol

## Project Overview

This project assigns a **credit score between 0 and 1000** to each wallet using historical transaction-level data from the Aave V2 protocol. The score reflects the reliability and behavior of wallets, where:

- **Higher scores** imply responsible, human-like usage
- **Lower scores** indicate risky, bot-like, or exploitative behavior

---

## Methodology

### 1. Data Loading

Raw JSON data of transactions is flattened and normalized using:

```python
load_and_flatten.load_normalized_data(json_path)
```

### 2. Feature Engineering

Key features are extracted per wallet:

* Count of actions: `deposit`, `borrow`, `repay`, `redeem`, `liquidation`
* Unique token count
* Active days
* Ratio-based heuristics

### 3. Heuristic Scoring

Before training, we generate a heuristic score (ground truth) based on:

* Rewarding repayments and deposits
* Penalizing liquidation calls and heavy borrowing

### 4. ML Model Training

A `RandomForestRegressor` is trained using:

* `X`: All features except wallet ID and score
* `y`: Heuristic score

### 5. Scoring New Wallets

The trained model assigns a credit score between 0 and 1000 to any wallet's historical transaction data.

### Folder Structure:-

WALLET_CREDIT_SCORE/
│
├── data/                         ← Raw JSON input
│   └── user-wallet-transactions.json
│
├── outputs/                      ← Outputs
│   ├── wallet_scores.csv         ← Final scored wallets
│   └── score_distribution.png    ← Score histogram
│
│
├── src/
│   ├── **score_wallets.py**          ←  One-step script
│   ├── load_and_flatten.py       ← JSON normalization
│   ├── feature_engineering.py    ← Feature extraction + scoring
│   └── scoring_model.py          ← ML model logic

|      └── check_distribution.py        ← distribution of wallets

|    ├── outputs/wallet_scores_ml.csv      ← ML predicted vs heuristic
│
├── README.md
└── analysis.md

## Run One-Step Pipeline:-

cd src

python score_wallets.py


## Requirements

pip install -r requirements.txt
