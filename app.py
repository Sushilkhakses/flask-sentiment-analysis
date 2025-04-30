from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    sentiment = None
    polarity = None
    subjectivity = None

    if request.method == 'POST':
        user_text = request.form['text']
        blob = TextBlob(user_text)
        polarity = round(blob.sentiment.polarity, 3)
        subjectivity = round(blob.sentiment.subjectivity, 3)

        if polarity > 0:
            sentiment = 'Positive'
        elif polarity < 0:
            sentiment = 'Negative'
        else:
            sentiment = 'Neutral'

        return render_template('index.html', text=user_text, sentiment=sentiment,
                               polarity=polarity, subjectivity=subjectivity)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)