import os 
import pandas as pd

HUMAN_PATH = "data/raw/wikipedia_human.csv"
AI_PATH = "data/raw/AI_topics.csv"

OUTPUT_PATH = "data/processed/dataset.csv"

os.makedirs("data/processed", exist_ok=True)

MIN_WORDS = 90
MAX_WORDS = 150


def filter_length(df):
    return df[
        (df["word_count"] >= MIN_WORDS) &
        (df["word_count"] <= MAX_WORDS)
    ]


human = pd.read_csv(HUMAN_PATH)
ai = pd.read_csv(AI_PATH)

print("Before:", len(human), len(ai))

human = filter_length(human)
ai = filter_length(ai)

print("After filter:", len(human), len(ai))

n = min(len(human), len(ai))

human = human.sample(n, random_state=42)
ai = ai.sample(n, random_state=42)

df = pd.concat([human, ai], ignore_index=True)

df = df.sample(frac=1, random_state=42).reset_index(drop=True)

df.to_csv(OUTPUT_PATH, index=False)

print("Saved:", len(df))