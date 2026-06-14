from transformers import pipeline

model = pipeline(
    "text-classification",
    model="crypter70/IndoBERT-Sentiment-Analysis"
)

samples = [
    "bagus sekali",
    "jelek sekali",
    "saya sangat kecewa",
    "saya sangat senang"
]

for text in samples:
    result = model(text)[0]
    print(text)
    print(result)
    print("-" * 50)