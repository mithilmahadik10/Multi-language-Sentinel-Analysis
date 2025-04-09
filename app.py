from flask import Flask, render_template, request
from googletrans import Translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

translator = Translator()
analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text, lang='en'):
    if lang != 'en':
        try:
            translated = translator.translate(text, dest='en')
            text = translated.text
        except Exception as e:
            return "Translation Error", {"error": str(e)}

    sentiment_scores = analyzer.polarity_scores(text)

    if sentiment_scores['compound'] >= 0.05:
        sentiment = 'Positive'
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'

    return sentiment, sentiment_scores

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    scores = None
    user_text = ""
    language = "en"
    error = None

    if request.method == "POST":
        user_text = request.form["text"]
        language = request.form["language"]
        result, scores = analyze_sentiment(user_text, language)

        if result == "Translation Error":
            error = scores["error"]
            result, scores = None, None

    return render_template("index.html", sentiment=result, scores=scores, text=user_text, lang=language, error=error)

if __name__ == "__main__":
    app.run(debug=True)
