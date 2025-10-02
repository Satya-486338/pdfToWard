import os
import subprocess
from tkinter import Tk, filedialog, messagebox

def get_unique_filename(base_path, extension):
    counter = 1
    new_path = base_path + extension
    while os.path.exists(new_path):
        new_path = f"{base_path}_{counter}{extension}"
        counter += 1
    return new_path

def process_pdf():
    input_pdf = filedialog.askopenfilename(title="Select PDF File", filetypes=[("PDF files", "*.pdf")])
    if not input_pdf:
        return

    output_folder = filedialog.askdirectory(title="Select Output Folder")
    if not output_folder:
        return

    base_name = os.path.splitext(os.path.basename(input_pdf))[0]
    output_pdf_base = os.path.join(output_folder, base_name + '_searchable')
    output_pdf = get_unique_filename(output_pdf_base, '.pdf')

    try:
        subprocess.run([
            'ocrmypdf', '--output-type', 'pdf',
            '-l', 'hin+eng', input_pdf, output_pdf
        ], check=True)

        messagebox.showinfo("Success", f"OCR completed:\n{output_pdf}")
    except Exception as e:
        if os.path.exists(output_pdf):
            try:
                os.remove(output_pdf)
            except:
                pass
        messagebox.showerror("Error", f"OCR failed:\n{str(e)}")

# GUI setup
root = Tk()
root.title("OCR PDF Generator")
root.geometry("360x180")
root.resizable(False, False)

from tkinter import Button, Label
Label(root, text="Generate Searchable PDF with OCR (Hindi + English)", pady=20).pack()
Button(root, text="Select PDF and Output Folder", command=process_pdf).pack(pady=10)

root.mainloop()