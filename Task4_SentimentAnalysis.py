from textblob import TextBlob
import pandas as pd

reviews = [
    "Amazing product",
    "Very bad quality",
    "Worth the money",
    "Terrible experience",
    "Excellent item",
    "Not good"
]

results = []

for review in reviews:

    polarity = TextBlob(review).sentiment.polarity

    if polarity > 0:
        sentiment = "Positive"

    elif polarity < 0:
        sentiment = "Negative"

    else:
        sentiment = "Neutral"

    results.append([review, sentiment])

df = pd.DataFrame(
    results,
    columns=["Review", "Sentiment"]
)

print(df)

df.to_csv("sentiment_output.csv", index=False)