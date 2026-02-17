from flask import Flask, request, render_template_string
from textblob import TextBlob

app = Flask(__name__)

# This is the "Face" of your app (HTML/CSS)
HTML_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>AI Hackathon Project</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; background-color: #eef2f3; padding-top: 50px; }
        .box { background: white; padding: 40px; border-radius: 15px; display: inline-block; shadow: 0 4px 6px rgba(0,0,0,0.1); }
        input { padding: 12px; width: 300px; border: 1px solid #ccc; border-radius: 5px; margin-bottom: 10px; }
        button { padding: 12px 25px; background: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; }
        .result { margin-top: 20px; font-size: 1.5em; color: #333; }
    </style>
</head>
<body>
    <div class="box">
        <h1>🧠 AI Sentiment Analyzer</h1>
        <p>Type how you feel and let the AI decide the tone.</p>
        <form method="POST">
            <input type="text" name="user_text" placeholder="Enter a sentence..." required> <br>
            <button type="submit">Analyze Now</button>
        </form>
        {% if sentiment %}
            <div class="result">Analysis: <strong>{{ sentiment }}</strong></div>
        {% endif %}
    </div>
</body>
</html>
'''

@app.route('/', methods=['GET', 'POST'])
def home():
    sentiment = None
    if request.method == 'POST':
        user_input = request.form['user_text']
        # The AI Logic
        analysis = TextBlob(user_input)
        if analysis.sentiment.polarity > 0:
            sentiment = "Positive 😊"
        elif analysis.sentiment.polarity < 0:
            sentiment = "Negative 😡"
        else:
            sentiment = "Neutral 😐"
    return render_template_string(HTML_PAGE, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)