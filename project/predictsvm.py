import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download NLTK data (needed for preprocessing)
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Load trained model and vectorizer
with open("svm_model.pkl", "rb") as f:
    model = pickle.load(f)
with open("vectorizer.pkl", "rb") as f:
    cv = pickle.load(f)

# Preprocessing function (must match training)
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = text.lower()
    text = "".join([c for c in text if c not in string.punctuation])
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(words)

# Prediction loop
while True:
    review = input("\nEnter your review (or type 'exit' to quit): ")
    if review.lower() == "exit":
        break
    review_clean = preprocess(review)
    review_vector = cv.transform([review_clean])
    prediction = model.predict(review_vector)[0]
    print(f"📝 Prediction: {prediction}")
