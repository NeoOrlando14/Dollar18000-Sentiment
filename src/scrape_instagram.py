import os
import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By


POST_URL = "https://www.instagram.com/p/DZjkJ1-Jh5R/"


def scrape_instagram_comments():

    driver = webdriver.Chrome()

    print("Membuka Instagram...")
    driver.get("https://www.instagram.com/")

    print("\n=== LOGIN INSTAGRAM ===")
    print("1. Login Instagram")
    print("2. Buka postingan")
    print("3. Klik tombol + / View More Comments sampai habis")
    print("4. Scroll panel komentar kanan sampai bawah")
    input("\nKalau semua komentar sudah tampil, tekan ENTER...")

    driver.get(POST_URL)

    time.sleep(8)

    print("\nTunggu 10 detik...")
    print("Klik tombol + sebanyak mungkin jika masih ada.")

    time.sleep(10)

    spans = driver.find_elements(By.TAG_NAME, "span")

    print(f"\nJumlah span ditemukan: {len(spans)}")

    comments = []

    blacklist = [
        "see translation",
        "view replies",
        "contact uploading",
        "non-users",
        "english",
        "afrikaans",
        "meta",
        "instagram"
    ]

    for span in spans:

        try:

            text = span.text.strip()

            if not text:
                continue

            skip = False

            for item in blacklist:

                if item in text.lower():
                    skip = True
                    break

            if skip:
                continue

            comments.append(text)

        except:
            pass

    print(f"\nTotal komentar mentah: {len(comments)}")

    current_dir = os.path.dirname(
        os.path.abspath(__file__)
    )

    project_root = os.path.dirname(
        current_dir
    )

    output_file = os.path.join(
        project_root,
        "data",
        "instagram_comments.csv"
    )

    df = pd.DataFrame({
        "source": ["instagram"] * len(comments),
        "text": comments
    })

    df.to_csv(
        output_file,
        index=False,
        encoding="utf-8-sig"
    )

    print("\n=== SELESAI ===")
    print(f"Total data tersimpan: {len(comments)}")
    print(output_file)

    driver.quit()


if __name__ == "__main__":
    scrape_instagram_comments()
