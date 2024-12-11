import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfMerger

# Global list to store PDF file paths
pdf_files = []


# Function to add PDFs
def add_pdf():
    files = filedialog.askopenfilenames(
        title="Select PDF Files",
        filetypes=[("PDF Files", "*.pdf")]
    )
    if files:
        pdf_files.extend(files)
        update_pdf_list()


# Function to update the list display
def update_pdf_list():
    pdf_list_display.delete(0, tk.END)
    for pdf in pdf_files:
        pdf_list_display.insert(tk.END, os.path.basename(pdf))


# Function to clear selected PDFs
def clear_list():
    global pdf_files
    pdf_files = []
    pdf_list_display.delete(0, tk.END)


# Function to merge PDFs
def merge_pdfs():
    if not pdf_files:
        messagebox.showerror("Error", "No PDF files selected!")
        return

    save_location = filedialog.askdirectory(title="Select Save Location")
    if not save_location:
        return

    merged_file_name = file_name_entry.get().strip()
    if not merged_file_name:
        messagebox.showerror("Error", "Please specify a file name!")
        return

    try:
        merger = PdfMerger()
        for pdf in pdf_files:
            merger.append(pdf)

        output_path = os.path.join(save_location, f"{merged_file_name}.pdf")
        merger.write(output_path)
        merger.close()

        messagebox.showinfo("Success", f"Merged PDF saved as: {output_path}")
        clear_list()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


# Create main tkinter window
app = tk.Tk()
app.title("Finlay - PDF Merger")
app.geometry("600x700")
app.configure(bg="#1e1e2e")
app.resizable(False, False)

# Title Label
title_label = tk.Label(
    app, text="Finlay", font=("Helvetica", 24, "bold"), fg="#ff79c6", bg="#1e1e2e"
)
title_label.pack(pady=10)

# Add PDF Button
add_button = tk.Button(
    app,
    text="Upload PDFs",
    command=add_pdf,
    font=("Arial", 14),
    bg="#6272a4",
    fg="white",
    width=15,
)
add_button.pack(pady=10)

# List of PDFs
pdf_list_frame = tk.Frame(app, bg="#1e1e2e")
pdf_list_frame.pack(pady=10)

pdf_list_label = tk.Label(
    pdf_list_frame, text="Selected PDFs:", font=("Arial", 12), fg="white", bg="#1e1e2e"
)
pdf_list_label.pack(anchor="w")

pdf_list_display = tk.Listbox(
    pdf_list_frame, width=50, height=10, font=("Arial", 12), bg="#282a36", fg="white"
)
pdf_list_display.pack(pady=5)

# Clear Button
clear_button = tk.Button(
    app,
    text="Clear List",
    command=clear_list,
    font=("Arial", 12),
    bg="#ff5555",
    fg="white",
    width=15,
)
clear_button.pack(pady=5)

# File Name Input
file_name_frame = tk.Frame(app, bg="#1e1e2e")
file_name_frame.pack(pady=10)

file_name_label = tk.Label(
    file_name_frame, text="Merged File Name:", font=("Arial", 12), fg="white", bg="#1e1e2e"
)
file_name_label.pack(side="left", padx=5)

file_name_entry = tk.Entry(file_name_frame, font=("Arial", 12), width=30, bg="#44475a", fg="white")
file_name_entry.pack(side="left", padx=5)

# Merge Button
merge_button = tk.Button(
    app,
    text="Merge PDFs",
    command=merge_pdfs,
    font=("Arial", 14),
    bg="#50fa7b",
    fg="black",
    width=20,
)
merge_button.pack(pady=20)

# Run the app
app.mainloop()
