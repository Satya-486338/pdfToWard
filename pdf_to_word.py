import os
import subprocess
from tkinter import Tk, filedialog, messagebox
from pdf2docx import Converter
from docx import Document

def get_unique_filename(base_path, extension):
    counter = 1
    new_path = base_path + extension
    while os.path.exists(new_path):
        new_path = f"{base_path}_{counter}{extension}"
        counter += 1
    return new_path

def contains_text(docx_path):
    try:
        doc = Document(docx_path)
        return any(p.text.strip() for p in doc.paragraphs)
    except Exception:
        return False

def process_pdf():
    input_pdf = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])
    if not input_pdf:
        return

    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return

    ocr_pdf = os.path.join(output_folder, 'ocr_output.pdf')
    base_name = os.path.splitext(os.path.basename(input_pdf))[0]
    output_docx_base = os.path.join(output_folder, base_name + '_output')
    output_docx = get_unique_filename(output_docx_base, '.docx')

    try:
        subprocess.run(['ocrmypdf', '--output-type', 'pdf', '-l', 'hin+eng', input_pdf, ocr_pdf], check=True)

        cv = Converter(ocr_pdf)
        cv.convert(output_docx, start=0, end=None)
        cv.close()

        if not contains_text(output_docx):
            os.remove(output_docx)
            raise ValueError("Conversion completed but output contains no text. Likely image-only content.")

        os.remove(ocr_pdf)
        messagebox.showinfo("Success", f"Word file created:\n{output_docx}")

    except Exception as e:
        # Cleanup intermediate files
        for f in [ocr_pdf, output_docx]:
            if os.path.exists(f):
                try:
                    os.remove(f)
                except:
                    pass
        messagebox.showerror("Error", f"Conversion failed:\n{str(e)}")

# GUI setup
root = Tk()
root.title("PDF to Word Converter")
root.geometry("350x180")
root.resizable(False, False)

from tkinter import Button, Label
Label(root, text="Convert PDF to Word with OCR", pady=20).pack()
Button(root, text="Select PDF and Output Folder", command=process_pdf).pack(pady=10)

root.mainloop()