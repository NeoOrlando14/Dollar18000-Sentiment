import os
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def create_visualization():

    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    project_root = os.path.dirname(
        current_dir
    )

    data_folder = os.path.join(
        project_root,
        "data"
    )

    output_folder = os.path.join(
        project_root,
        "output"
    )

    os.makedirs(
        output_folder,
        exist_ok=True
    )

    sentiment_path = os.path.join(
        data_folder,
        "final_sentiment.csv"
    )

    keyword_path = os.path.join(
        data_folder,
        "keywords.csv"
    )

    df = pd.read_csv(sentiment_path)

    keyword_df = pd.read_csv(keyword_path)

    # =========================
    # Grafik Sentimen
    # =========================

    sentiment_counts = (
        df["sentiment"]
        .value_counts()
    )

    plt.figure(figsize=(8, 5))

    sentiment_counts.plot(
        kind="bar"
    )

    plt.title(
        "Sentiment Analysis Result"
    )

    plt.xlabel(
        "Sentiment"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_folder,
            "sentiment_comparison.png"
        )
    )

    plt.close()

    # =========================
    # Grafik Keyword
    # =========================

    plt.figure(figsize=(10, 6))

    top10 = keyword_df.head(10)

    plt.bar(
        top10["keyword"],
        top10["frequency"]
    )

    plt.title(
        "Top 10 Keywords"
    )

    plt.xlabel(
        "Keyword"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.xticks(
        rotation=45
    )

    plt.tight_layout()

    plt.savefig(
        os.path.join(
            output_folder,
            "keyword_frequency.png"
        )
    )

    plt.close()

    # =========================
    # WordCloud
    # =========================

    text = " ".join(
        df["clean_text"]
        .astype(str)
    )

    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color="white"
    ).generate(text)

    wordcloud.to_file(
        os.path.join(
            output_folder,
            "wordcloud.png"
        )
    )

    print("\n=== VISUALISASI BERHASIL ===")

    print(
        os.path.join(
            output_folder,
            "sentiment_comparison.png"
        )
    )

    print(
        os.path.join(
            output_folder,
            "keyword_frequency.png"
        )
    )

    print(
        os.path.join(
            output_folder,
            "wordcloud.png"
        )
    )


if __name__ == "__main__":
    create_visualization()