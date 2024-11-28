import os
import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

def get_attachments(reader):
    """
    Retrieves the file attachments of the PDF as a dictionary of file names
    and the file data as a bytestring. 
    :return: dictionary of filenames and bytestrings
    """
    catalog = reader.trailer["/Root"]
    embedded_files = catalog['/Names']['/EmbeddedFiles']['/Names']
    attachments = {}
    for i in range(0, len(embedded_files), 2):
        name = embedded_files[i]
        file_spec = embedded_files[i + 1].get_object()
        file_data = file_spec['/EF']['/F'].get_data()
        if not name.lower().endswith('.pdf'):
            name += '.pdf'
        attachments[name] = file_data

    return attachments

def save_attachments(pdf_path, save_directory):
    # Extract the base name of the PDF file without the extension
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]

    # Create a directory with the base name of the PDF file in the save directory
    save_path = os.path.join(save_directory, base_name)
    try:
        if not os.path.exists(save_path):
            os.makedirs(save_path)
    except PermissionError:
        messagebox.showerror("Permission Error", f"Permission denied: Cannot create directory '{save_path}'.")
        return

    # Open the PDF file
    try:
        with open(pdf_path, 'rb') as handler:
            reader = PyPDF2.PdfReader(handler)
            attachments = get_attachments(reader)

            # Save the attachments to files in the new directory
            for f_name, f_data in attachments.items():
                file_path = os.path.join(save_path, f_name)
                try:
                    with open(file_path, 'wb') as outfile:
                        outfile.write(f_data)
                except PermissionError:
                    messagebox.showerror("Permission Error", f"Permission denied: Cannot write file '{file_path}'.")
                    return
        messagebox.showinfo("Success", f"Attachments saved successfully in '{save_path}'.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def select_pdf_file():
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    pdf_entry.delete(0, tk.END)
    pdf_entry.insert(0, file_path)

    # Update the default save directory entry with the directory of the selected PDF file
    default_save_directory = os.path.dirname(file_path)
    save_entry.delete(0, tk.END)
    save_entry.insert(0, default_save_directory)

def select_save_directory():
    directory = filedialog.askdirectory()
    save_entry.delete(0, tk.END)
    save_entry.insert(0, directory)

def on_extract():
    pdf_path = pdf_entry.get()
    save_directory = save_entry.get()
    if not pdf_path or not save_directory:
        messagebox.showerror("Input Error", "Please provide both the PDF file path and the save directory.")
        return
    save_attachments(pdf_path, save_directory)

    # Clear the input fields after extraction
    pdf_entry.delete(0, tk.END)
    save_entry.delete(0, tk.END)

# Create the main Tkinter window
root = tk.Tk()
root.title("PDF Attachment Extractor")

# PDF file path entry
tk.Label(root, text="PDF File:").grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)
pdf_entry = tk.Entry(root, width=50)
pdf_entry.grid(row=0, column=1, padx=10, pady=5)
tk.Button(root, text="Browse...", command=select_pdf_file).grid(row=0, column=2, padx=10, pady=5)

# Save directory entry
tk.Label(root, text="Save Directory:").grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)
save_entry = tk.Entry(root, width=50)
save_entry.grid(row=1, column=1, padx=10, pady=5)
tk.Button(root, text="Browse...", command=select_save_directory).grid(row=1, column=2, padx=10, pady=5)

# Extract button
tk.Button(root, text="Extract Attachments", command=on_extract).grid(row=2, columnspan=3, pady=10)

# Run the Tkinter event loop
basedir = os.path.dirname(__file__)
root.iconbitmap(os.path.join(basedir, "icons", "icon.ico"))
root.mainloop()
