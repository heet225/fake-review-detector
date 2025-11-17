# Fake Review Detector

A machine learning-based web application that detects whether a product review is genuine or fake using Support Vector Machine (SVM) classification.

## Features

- **Web Interface**: User-friendly Flask web application for easy review submission
- **ML-Powered Detection**: SVM classifier trained on a dataset of labeled reviews
- **Text Preprocessing**: Advanced NLP techniques including tokenization, lemmatization, and stopword removal
- **High Accuracy**: Achieves ~86% accuracy on test data
- **Command-Line Tool**: Optional CLI for batch prediction

## Project Structure

```
fake-review-detector/
├── requirements.txt           # Python dependencies
├── README.md                 # This file
└── project/
    ├── app.py                # Flask web application
    ├── trainsvm.py           # Model training script
    ├── predictsvm.py         # Command-line prediction tool
    ├── fake reviews dataset.csv  # Training dataset
    ├── svm_model.pkl         # Trained SVM model
    ├── vectorizer.pkl        # CountVectorizer for text transformation
    └── templates/
        └── index.html        # Web interface template
```

## Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

## Installation

1. **Clone the repository** (if not already done):
   ```bash
   git clone https://github.com/heet225/fake-review-detector.git
   cd fake-review-detector
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK data** (will be automatically downloaded on first run, but you can also do it manually):
   ```python
   python3 -c "import nltk; nltk.download('stopwords'); nltk.download('punkt'); nltk.download('wordnet')"
   ```

## Usage

### Option 1: Automated Setup (Recommended - Works on all platforms)

**Using Python script (Windows, macOS, Linux):**
```bash
python3 run.py
```
or
```bash
python run.py
```

This script will automatically:
- Check your Python version
- Install all required dependencies
- Verify model files exist
- Start the Flask web application

### Option 2: Using Shell Script (macOS/Linux only)

```bash
./run.sh
```

### Option 3: Manual Setup

1. **Install dependencies first**:
   ```bash
   pip install -r requirements.txt
   ```
   or
   ```bash
   pip3 install -r requirements.txt
   ```

2. **Navigate to the project directory**:
   ```bash
   cd project
   ```

3. **Run the Flask application**:
   ```bash
   python3 app.py
   ```

4. **Open your browser** and visit:
   ```
   http://127.0.0.1:5000
   ```

5. **Enter a review** in the text box and click "Check Review" to see if it's genuine or fake.

### Option 4: Command-Line Interface

**Important**: Install dependencies first before using CLI mode:
```bash
pip install -r requirements.txt
```

Then:

1. **Navigate to the project directory**:
   ```bash
   cd project
   ```

2. **Run the prediction script**:
   ```bash
   python3 predictsvm.py
   ```

3. **Enter reviews** when prompted. Type 'exit' to quit.

## Training the Model

If you want to retrain the model with your own dataset or different parameters:

1. **Navigate to the project directory**:
   ```bash
   cd project
   ```

2. **Run the training script**:
   ```bash
   python3 trainsvm.py
   ```

   This will:
   - Load the dataset from `fake reviews dataset.csv`
   - Preprocess the text data
   - Train an SVM classifier
   - Display accuracy metrics and classification report
   - Save the trained model and vectorizer as `.pkl` files

## Model Performance

- **Accuracy**: ~86%
- **Model**: Linear Support Vector Classifier (LinearSVC)
- **Features**: Bag-of-words representation using CountVectorizer
- **Text Processing**: Lowercasing, punctuation removal, tokenization, lemmatization, stopword removal

## Dataset

The model is trained on a dataset of labeled product reviews:
- **CG (Computer Generated)**: Fake reviews
- **OR (Original)**: Real reviews

## Dependencies

- **Flask** (3.0.0): Web framework
- **scikit-learn** (1.3.2): Machine learning library
- **pandas** (2.1.3): Data manipulation
- **nltk** (3.8.1): Natural language processing toolkit

## How It Works

1. **Text Preprocessing**:
   - Convert text to lowercase
   - Remove punctuation
   - Tokenize into words
   - Lemmatize words to their root form
   - Remove common stopwords (e.g., "the", "is", "and")

2. **Feature Extraction**:
   - Convert preprocessed text to numerical features using CountVectorizer
   - Create a bag-of-words representation

3. **Classification**:
   - Use trained Linear SVM model to predict if review is Real or Fake
   - Return prediction with confidence

## Examples

### Real Review Example:
```
"This product exceeded my expectations. The quality is excellent and it works exactly as described. Highly recommended!"
```
**Prediction**: Real

### Fake Review Example:
```
"Amazing! Best ever! Must buy! 5 stars!!!"
```
**Prediction**: Fake

## Troubleshooting

### ❌ ModuleNotFoundError: No module named 'flask' (or sklearn, pandas, nltk)

**Solution**: You need to install dependencies first!

```bash
# Try one of these commands:
pip install -r requirements.txt
# or
pip3 install -r requirements.txt
# or
python -m pip install -r requirements.txt
# or
python3 -m pip install -r requirements.txt
```

**Best Solution**: Use the automated startup script:
```bash
python3 run.py
```

This script automatically installs dependencies for you.

### Port Already in Use
If port 5000 is already in use, you can change it in `project/app.py`:
```python
app.run(debug=True, port=5001)  # Change port to 5001 or any available port
```

### Permission Denied on Installation
If you get permission errors when installing packages:
```bash
pip install --user -r requirements.txt
```

### NLTK Data Not Found
If you get NLTK data errors, manually download required packages:
```python
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
```

### Script Won't Run (./run.sh: Permission denied)
Make the script executable:
```bash
chmod +x run.sh
```

Or use the Python script instead (works on all platforms):
```bash
python3 run.py
```

## Future Improvements

- Add support for more sophisticated models (BERT, transformer-based)
- Implement confidence scores
- Add multilingual support
- Create REST API endpoints
- Add batch processing capabilities
- Implement model versioning and A/B testing

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available for educational purposes.

## Authors

- Heet225

## Acknowledgments

- Dataset contributors
- scikit-learn and NLTK communities
- Flask framework developers
