# Dollar18000-Sentiment

## Deskripsi

Proyek ini bertujuan untuk membandingkan narasi media massa dan opini publik Instagram terkait isu ekonomi, khususnya pemberitaan mengenai kondisi ekonomi global dan dampaknya terhadap Indonesia.

Analisis dilakukan menggunakan scraping berita, scraping komentar Instagram, preprocessing data, analisis sentimen menggunakan IndoBERT, analisis kata kunci, serta visualisasi hasil.

---

## Dataset

### Media Massa

Sumber:
https://finance.detik.com/berita-ekonomi-bisnis/d-8529746/ekonomi-global-bikin-cemas-ri-gimana

### Instagram

Sumber:
https://www.instagram.com/p/DZjkJ1-Jh5R/

---

## Library yang Digunakan

* pandas
* requests
* beautifulsoup4
* selenium
* transformers
* torch
* matplotlib
* wordcloud
* webdriver-manager
* newspaper3k
* python-dotenv

---

## Instalasi

```bash
pip install -r requirements.txt
```

## Cara Menjalankan

### 1. Scraping Berita

```bash
python src/scrape_news.py
```

Output:

```text
data/news.csv
```

### 2. Scraping Instagram

```bash
python src/scrape_instagram.py
```

Output:

```text
data/instagram_comments.csv
```

### 3. Preprocessing

```bash
python src/preprocessing.py
```

Output:

```text
data/final_sentiment.csv
```

### 4. Sentiment Analysis

```bash
python src/sentiment_analysis.py
```

Output:

```text
data/final_sentiment.csv
```

### 5. Keyword Analysis

```bash
python src/keyword_analysis.py
```

Output:

```text
data/keywords.csv
```

### 6. Visualisasi

```bash
python src/visualization.py
```

Output:

```text
output/sentiment_comparison.png
output/keyword_frequency.png
output/wordcloud.png
```

---

## Struktur Folder

Dollar18000-Sentiment/

* data/
* output/
* src/
* requirements.txt
* README.md

---

## Output Akhir

* Sentiment Analysis Result
* Keyword Frequency
* WordCloud
* Dataset hasil analisis
