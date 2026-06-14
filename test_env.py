from dotenv import load_dotenv
import os

load_dotenv()

username = os.getenv("IG_USERNAME")
password = os.getenv("IG_PASSWORD")

print("Username:", username)

if password:
    print("Password berhasil dibaca dari .env")
else:
    print("Password tidak ditemukan")