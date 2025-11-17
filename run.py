#!/usr/bin/env python3
"""
Fake Review Detector - Cross-platform Startup Script

This script works on Windows, macOS, and Linux.
It checks dependencies, installs them if needed, and starts the Flask app.
"""

import sys
import subprocess
import os
from pathlib import Path

def print_banner():
    """Print the application banner."""
    print("=" * 50)
    print("  Fake Review Detector")
    print("=" * 50)
    print()

def check_python_version():
    """Check if Python version is adequate."""
    if sys.version_info < (3, 7):
        print("❌ Error: Python 3.7 or higher is required.")
        print(f"   Current version: {sys.version}")
        sys.exit(1)
    print(f"✓ Python version: {sys.version.split()[0]}")

def check_and_install_dependencies():
    """Check if dependencies are installed, and install them if not."""
    print("\nChecking dependencies...")
    
    try:
        import flask
        import sklearn
        import pandas
        import nltk
        print("✓ All dependencies are installed")
        return True
    except ImportError as e:
        print(f"⚠ Missing dependencies detected: {e.name}")
        print("\nInstalling dependencies...")
        
        # Get the directory where this script is located
        script_dir = Path(__file__).parent
        requirements_file = script_dir / "requirements.txt"
        
        if not requirements_file.exists():
            print(f"❌ Error: requirements.txt not found at {requirements_file}")
            sys.exit(1)
        
        try:
            # Try to install packages
            subprocess.check_call([
                sys.executable, "-m", "pip", "install", "-r", str(requirements_file)
            ])
            print("✓ Dependencies installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("\n❌ Error: Failed to install dependencies automatically.")
            print("\nPlease install them manually by running:")
            print(f"   {sys.executable} -m pip install -r requirements.txt")
            print("\nOr:")
            print(f"   pip3 install -r requirements.txt")
            sys.exit(1)

def check_model_files():
    """Check if model files exist."""
    script_dir = Path(__file__).parent
    project_dir = script_dir / "project"
    
    model_file = project_dir / "svm_model.pkl"
    vectorizer_file = project_dir / "vectorizer.pkl"
    
    if not model_file.exists() or not vectorizer_file.exists():
        print("\n⚠ Model files not found. Training model...")
        print("This may take a few moments...")
        
        train_script = project_dir / "trainsvm.py"
        if not train_script.exists():
            print(f"❌ Error: Training script not found at {train_script}")
            sys.exit(1)
        
        try:
            subprocess.check_call([sys.executable, str(train_script)], cwd=str(project_dir))
            print("✓ Model trained successfully")
        except subprocess.CalledProcessError:
            print("❌ Error: Failed to train model")
            sys.exit(1)
    else:
        print("✓ Model files found")

def start_flask_app():
    """Start the Flask application."""
    script_dir = Path(__file__).parent
    project_dir = script_dir / "project"
    app_script = project_dir / "app.py"
    
    if not app_script.exists():
        print(f"❌ Error: Flask app not found at {app_script}")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("  Starting Flask application...")
    print("=" * 50)
    print("\n  🌐 Access the app at: http://127.0.0.1:5000")
    print("  Press CTRL+C to quit")
    print("\n" + "=" * 50)
    print()
    
    try:
        subprocess.check_call([sys.executable, str(app_script)], cwd=str(project_dir))
    except KeyboardInterrupt:
        print("\n\n✓ Application stopped by user")
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error: Flask application failed with exit code {e.returncode}")
        sys.exit(1)

def main():
    """Main function to run the startup sequence."""
    print_banner()
    check_python_version()
    check_and_install_dependencies()
    check_model_files()
    start_flask_app()

if __name__ == "__main__":
    main()
