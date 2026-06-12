import os
import re
import time
import pandas as pd
import requests
from topics import TOPICS

OUTPUT_PATH = "data/raw/wikipedia_human.csv"
TARGET = 300

HEADERS = {
    "User-Agent": "COMP8420AssignmentBot/1.0"
}


def clean_text(text):
    text = re.sub(r"\[\d+\]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def valid(text, min_words=80, max_words=200):
    wc = len(text.split())
    return min_words <= wc <= max_words


def fetch_text(topic):

    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "extracts",
        "explaintext": True,
        "titles": topic
    }

    r = requests.get(url, params=params, headers=HEADERS)
    r.raise_for_status()

    data = r.json()

    page = next(iter(data["query"]["pages"].values()))
    return page.get("extract", "")


def split_paragraphs(text):

    parts = text.split("\n")

    out = []

    for p in parts:
        p = clean_text(p)
        if valid(p):
            out.append(p)

    return out


def main():

    os.makedirs("data/raw", exist_ok=True)

    rows = []
    sample_id = 1

    for topic in TOPICS:

        if len(rows) >= TARGET:
            break

        try:

            text = fetch_text(topic)

            paragraphs = split_paragraphs(text)

            for p in paragraphs:

                if len(rows) >= TARGET:
                    break

                rows.append({
                    "id": sample_id,
                    "topic": topic,
                    "text": p,
                    "label": 0,
                    "source": "wikipedia",
                    "word_count": len(p.split())
                })

                sample_id += 1

            print(topic, len(rows))

            time.sleep(0.5)

        except Exception as e:
            print("error", topic, e)

    df = pd.DataFrame(rows)

    df.to_csv(OUTPUT_PATH, index=False)

    print("Saved", len(df))


if __name__ == "__main__":
    main()