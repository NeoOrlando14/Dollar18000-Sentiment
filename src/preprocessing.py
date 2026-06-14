import os
import re
import pandas as pd


def clean_text(text):

    text = str(text)

    text = text.lower()

    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)

    text = re.sub(r"@\w+", "", text)

    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


def preprocess_data():

    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    project_root = os.path.dirname(
        current_dir
    )

    news_path = os.path.join(
        project_root,
        "data",
        "news.csv"
    )

    instagram_path = os.path.join(
        project_root,
        "data",
        "instagram_comments.csv"
    )

    news_df = pd.read_csv(news_path)

    instagram_df = pd.read_csv(instagram_path)

    if "title" in news_df.columns:

        news_df["text"] = (
            news_df["title"].fillna("")
            + " "
            + news_df["text"].fillna("")
        )

    news_df = news_df[["source", "text"]]

    df = pd.concat(
        [news_df, instagram_df],
        ignore_index=True
    )

    blacklist = [
        "view replies",
        "see translation",
        "contact uploading",
        "non users",
        "english afrikaans",
        "meta"
    ]

    for item in blacklist:

        df = df[
            ~df["text"]
            .astype(str)
            .str.lower()
            .str.contains(item)
        ]

    df["clean_text"] = df["text"].apply(
        clean_text
    )

    df = df.drop_duplicates(
        subset=["clean_text"]
    )

    df = df[
        df["clean_text"].str.len() > 5
    ]

    output_path = os.path.join(
        project_root,
        "data",
        "final_sentiment.csv"
    )

    df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )

    print("\n=== SELESAI ===")
    print(df.head())
    print(f"\nTotal data: {len(df)}")
    print(output_path)


if __name__ == "__main__":
    preprocess_data()
