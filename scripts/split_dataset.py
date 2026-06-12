import pandas as pd
from sklearn.model_selection import train_test_split
import os


INPUT_PATH = "data/processed/dataset.csv"

train_out = "data/processed/train.csv"
val_out = "data/processed/val.csv"
test_out = "data/processed/test.csv"

df = pd.read_csv(INPUT_PATH)

train_df, temp_df = train_test_split(
    df,
    test_size=0.30,
    stratify=df["label"],
    random_state=42
)

val_df, test_df = train_test_split(
    temp_df,
    test_size=0.50,
    stratify=temp_df["label"],
    random_state=42
)

train_df.to_csv(train_out, index=False, encoding="utf-8")
val_df.to_csv(val_out, index=False, encoding="utf-8")
test_df.to_csv(test_out, index=False, encoding="utf-8")

print(f"saved {len(train_df)} samples to {train_out}")
print(f"saved {len(val_df)} samples to {val_out}")
print(f"saved {len(test_df)} samples to {test_out}")
