# pdfToWard
# 📝 PDF to Word Converter with OCR (Hindi + English)

This is a simple Windows GUI app built with Python that:
- Lets you select a PDF file and output folder
- Runs OCR using Tesseract (Hindi + English)
- Converts the searchable PDF to a Word document
- Deletes the intermediate OCR file

---

## 📂 Features

- GUI interface using Tkinter
- OCR support for Hindi and English via OCRmyPDF
- Converts PDF to Word using pdf2docx
- Output saved in user-selected folder

---

## 🛠️ Requirements

- Windows 64-bit
- Python 3.8+
- Tesseract OCR (with `hin` and `eng` trained data)
- Ghostscript (for OCRmyPDF)
- Installed Python packages:

---

## 📥 Installation

1. **Install Tesseract OCR**
 - Download from: https://github.com/tesseract-ocr/tesseract
 - Add to system PATH
 - Place `hin.traineddata` and `eng.traineddata` in `tessdata` folder

2. **Install Ghostscript**
 - Download from: https://www.ghostscript.com/download/gsdnld.html
 - Add to system PATH

3. **Install Python packages**
 ```bash
 pip install -r requirements.txt
 ```

Packaging for Windows (.exe)
Once you're happy with the script, turn it into a Windows app:
pip install pyinstaller
pyinstaller --onefile --windowed your_script.py


This creates a .exe file in the dist folder that runs your GUI on any Windows 64-bit system.

Want to add features like language selection, progress bar, or batch conversion next? I’d love to help you build it out!



