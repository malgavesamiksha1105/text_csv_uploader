from flask import Flask, request, jsonify
import pandas as pd
from textblob import TextBlob

app = Flask(__name__)

def get_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

@app.route('/analyze', methods=['POST'])
def analyze():
    file = request.files['file']
    df = pd.read_csv(file)

    results = []
    counts = {"Positive":0, "Negative":0, "Neutral":0, "Spam":0}

    for review in df['review']:
        sentiment = get_sentiment(str(review))
        results.append({"review": review, "sentiment": sentiment})
        counts[sentiment] += 1

    return jsonify({
        "results": results,
        "counts": counts
    })

if __name__ == '__main__':
    app.run(debug=True)
