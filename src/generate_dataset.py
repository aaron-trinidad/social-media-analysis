import os

import numpy as np
import pandas as pd

# Initialize seed
np.random.seed(42)

# Number of records in the dataset
n = 1000

# Lists of categories and sentiments
categories = ["Entertainment", "Politics", "Tech", "Sports"]
category_weights = {"Entertainment": 0.9, "Politics": 1.0, "Tech": 0.5, "Sports": 0.6}
sentiments = ["positive", "neutral", "negative"]

# Generate synthetic data
data = {
    "user_id": np.random.randint(1, 200, size=n),
    "category": np.random.choice(categories, size=n),
    "followers": np.random.randint(50, 100000, size=n),
    # "likes": np.random.poisson(lam=150, size=n),
    # "retweets": np.random.poisson(lam=30, size=n),
    "sentiment": np.random.choice(sentiments, size=n, p=[0.25, 0.3, 0.45]),
    "posted_hour": np.random.randint(0, 24, size=n),
}

df = pd.DataFrame(data)

# Generate likes and retweets based on followers
df["likes"] = np.random.poisson(lam=df["followers"] / 500, size=n).clip(0, None)
df["retweets"] = np.random.poisson(lam=df["likes"] / 10, size=n).clip(0, None)


df["weight"] = df["category"].map(category_weights)

# Introduce null values (in ~3% of rows for some columns)
for col in ["category", "sentiment"]:
    n_missing = int(0.03 * n)
    missing_idx = np.random.choice(df.index, n_missing, replace=False)
    df.loc[missing_idx, col] = np.nan

# Introduce outliers
# some users with millions of followers or exaggerated likes
outlier_idx = np.random.choice(df.index, 5, replace=False)
df.loc[outlier_idx, "followers"] = df["followers"].max() * 20
df.loc[outlier_idx, "likes"] = df["likes"].max() * 30

# Target variable (whether the tweet went viral)
df["viral"] = ((df["likes"].fillna(0) + 2 * df["retweets"]) * df["weight"] * 12) > (
    0.03 * df["followers"].fillna(1)
)
df["viral"] = df["viral"].astype(bool)

df.drop(columns="weight", inplace=True)

# Save dataset
output_path = "../data/tweets_synthetic.csv"
os.makedirs(os.path.dirname(output_path), exist_ok=True)
df.to_csv(output_path, index=False)

print(f"Dataset generated successfully at {output_path}")
print(df.head(10))
