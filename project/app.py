from flask import Flask, render_template, request
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')


with open("svm_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    cv = pickle.load(f)


stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = text.lower()
    text = "".join([c for c in text if c not in string.punctuation])
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(words)


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        review = request.form["review"]
        review_clean = preprocess(review)
        review_vector = cv.transform([review_clean])

        label_map = {"OG": "Real", "CG": "Fake"}
        prediction_raw = model.predict(review_vector)[0]
        prediction = label_map.get(prediction_raw, prediction_raw)

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
