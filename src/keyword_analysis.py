import os
import pandas as pd
from collections import Counter


def keyword_analysis():

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

    stopwords = {
        "yang", "dan", "di", "ke", "dari",
        "untuk", "ini", "itu", "karena",
        "ada", "akan", "atau", "juga",
        "sudah", "saja", "aja", "nya",
        "pak", "ri", "gimana"
    }

    all_text = " ".join(
        df["clean_text"].astype(str)
    )

    words = all_text.split()

    filtered_words = []

    for word in words:

        if (
            word not in stopwords
            and len(word) > 3
        ):
            filtered_words.append(word)

    counter = Counter(
        filtered_words
    )

    top_keywords = counter.most_common(20)

    keyword_df = pd.DataFrame(
        top_keywords,
        columns=[
            "keyword",
            "frequency"
        ]
    )

    output_path = os.path.join(
        project_root,
        "data",
        "keywords.csv"
    )

    keyword_df.to_csv(
        output_path,
        index=False,
        encoding="utf-8-sig"
    )

    print("\n=== TOP KEYWORDS ===")

    print(keyword_df)

    print("\nFile tersimpan:")
    print(output_path)


if __name__ == "__main__":
    keyword_analysis()