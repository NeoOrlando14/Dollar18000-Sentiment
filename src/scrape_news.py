from newspaper import Article
import pandas as pd
import os

URL = "https://finance.detik.com/berita-ekonomi-bisnis/d-8529746/ekonomi-global-bikin-cemas-ri-gimana"


def scrape_news():
    try:
        print("Mengambil artikel berita...")

        article = Article(URL, language="id")

        article.download()
        article.parse()

        current_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(current_dir)

        data_folder = os.path.join(project_root, "data")

        if not os.path.exists(data_folder):
            os.makedirs(data_folder)

        output_file = os.path.join(data_folder, "news.csv")

        df = pd.DataFrame({
            "source": ["media"],
            "title": [article.title],
            "text": [article.text]
        })

        df.to_csv(output_file, index=False, encoding="utf-8-sig")

        print("\n=== BERHASIL ===")
        print("Judul :", article.title)
        print("File  :", output_file)
        print("Data berhasil disimpan.")

    except Exception as e:
        print("\n=== ERROR ===")
        print(e)


if __name__ == "__main__":
    scrape_news()