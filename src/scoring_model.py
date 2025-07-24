from sklearn.ensemble import RandomForestRegressor

def train_model(X, y):
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    return model

def predict_score(model, X):
    return model.predict(X).clip(0, 1000)


def calculate_credit_score(features_df):
    score = (
        200
        + features_df["num_deposits"] * 10
        + features_df["num_repays"] * 20
        + features_df["active_days"] * 1
        - features_df["num_borrows"] * 5
        - features_df["num_liquidations"] * 100
    )
    features_df["credit_score"] = score.clip(0, 1000)
    return features_df


