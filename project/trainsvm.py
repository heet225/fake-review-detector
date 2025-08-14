import pandas as pd
import nltk
import string
import pickle
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Download required NLTK data
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Load dataset (make sure CSV is in same folder)
df = pd.read_csv("fake reviews dataset.csv")

# Change these names if your dataset uses different column headers
TEXT_COLUMN = "text"
LABEL_COLUMN = "label"
df[LABEL_COLUMN] = df[LABEL_COLUMN].replace({"OR": "Real", "CG": "Fake"})

# Preprocessing
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    text = text.lower()
    text = "".join([c for c in text if c not in string.punctuation])
    words = nltk.word_tokenize(text)
    words = [lemmatizer.lemmatize(w) for w in words if w not in stop_words]
    return " ".join(words)

df["cleaned_text"] = df[TEXT_COLUMN].apply(preprocess)

# Vectorization
cv = CountVectorizer()
X = cv.fit_transform(df["cleaned_text"])
y = df[LABEL_COLUMN]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train SVM model
model = LinearSVC()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
print(f"\n✅ Accuracy: {accuracy_score(y_test, y_pred):.2f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Save model & vectorizer
with open("svm_model.pkl", "wb") as f:
    pickle.dump(model, f)
with open("vectorizer.pkl", "wb") as f:
    pickle.dump(cv, f)

print("\n🎯 Model and vectorizer saved successfully!")
