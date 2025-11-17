# Quick Start Guide

## 🚀 Get Started in 2 Steps

### Step 1: Run the Automated Setup Script

**Option A: Python Script (Works on Windows, macOS, Linux)**
```bash
python3 run.py
```
or
```bash
python run.py
```

**Option B: Shell Script (macOS/Linux only)**
```bash
./run.sh
```

The script will automatically:
- ✅ Check Python version
- ✅ Install all dependencies
- ✅ Verify model files
- ✅ Start the web server

### Step 2: Open Your Browser
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

## 📱 Alternative: Manual Installation

If the automated script doesn't work, install manually:

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```
or
```bash
pip3 install -r requirements.txt
```

### Step 2: Run the App
```bash
cd project
python3 app.py
```

### Step 3: Open Browser
Navigate to: **http://127.0.0.1:5000**

## 📱 Command-Line Mode

For command-line predictions:
```bash
# First install dependencies
pip install -r requirements.txt

# Then run CLI
cd project
python3 predictsvm.py
```

## 🔧 Troubleshooting

**❌ ModuleNotFoundError: No module named 'flask'**
- You need to install dependencies first!
```bash
pip install -r requirements.txt
```
Or use the automated script:
```bash
python3 run.py
```

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

**Permission errors?**
- Try user installation:
```bash
pip install --user -r requirements.txt
```

---

For full documentation, see [README.md](README.md)
