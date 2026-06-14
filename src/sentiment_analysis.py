import os
import pandas as pd
from transformers import pipeline


def analyze_sentiment():

    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    project_root = os.path.dirname(
        current_dir
    )

    file_path = os.path.join(
        project_root,
        "data",
        "final_sentiment.csv"
    )

    df = pd.read_csv(file_path)

    print("Memuat model IndoBERT...")

    model = pipeline(
        "text-classification",
        model="crypter70/IndoBERT-Sentiment-Analysis"
    )

    sentiments = []
    scores = []

    for text in df["clean_text"]:

        result = model(
            str(text)[:512]
        )[0]

        label = result["label"]
        score = result["score"]

        if label.upper() == "POSITIVE":
            sentiment = "positive"
        elif label.upper() == "NEGATIVE":
            sentiment = "negative"
        else:
            sentiment = "neutral"

        sentiments.append(sentiment)
        scores.append(score)

        print(
            f"{sentiment} | {round(score,4)}"
        )

    df["sentiment"] = sentiments
    df["score"] = scores

    df.to_csv(
        file_path,
        index=False,
        encoding="utf-8-sig"
    )

    print("\n=== HASIL SENTIMEN ===")
    print(
        df["sentiment"]
        .value_counts()
    )

    print("\nFile tersimpan:")
    print(file_path)


if __name__ == "__main__":
    analyze_sentiment()