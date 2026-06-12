import pandas as pd

df1 = pd.read_csv("data/raw/wikipedia_human.csv")
df2 = pd.read_csv("data/raw/AI_Topics.csv")

df1_wc =df1["word_count"].describe()
df2_wc = df2["word_count"].describe()

df1_dup =df1.duplicated(subset=["text"]).sum()
df2_dup =df2.duplicated(subset=["text"]).sum()

print("Human data-size:", len(df1))
print("AI data-size:", len(df2))

print("\nHuman word count stats:")
print(df1_wc)       
print("\nAI word count stats:")
print(df2_wc)

print(f"\nHuman duplicates: {df1_dup}")
print(f"AI duplicates: {df2_dup}")