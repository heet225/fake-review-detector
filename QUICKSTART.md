# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
./run.sh
```

### Step 3: Open Your Browser
Navigate to: **http://127.0.0.1:5000**

---

## 📝 That's It!

The application will:
- ✅ Automatically check and install dependencies
- ✅ Download required NLTK data
- ✅ Load the pre-trained ML model
- ✅ Start the web server

## 🎯 Test the App

1. Enter any product review in the text box
2. Click "Check Review"
3. See if it's detected as **Real** or **Fake**

## 📱 Alternative: Command-Line Mode

For command-line predictions:
```bash
cd project
python3 predictsvm.py
```

## 🔧 Troubleshooting

**Port 5000 already in use?**
- Edit `project/app.py` and change the port:
```python
app.run(debug=True, port=5001)
```

**Dependencies not installing?**
- Try upgrading pip first:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

For full documentation, see [README.md](README.md)
