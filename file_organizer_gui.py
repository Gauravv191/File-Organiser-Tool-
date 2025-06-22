import os
import shutil
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox

# Extension to folder mapping
EXTENSION_MAP = {
    '.txt': 'TextFiles',
    '.pdf': 'PDFs',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.py': 'PythonScripts',
    '.docx': 'Documents',
    '.xlsx': 'Spreadsheets',
}

def organize_files(folder_path, status_label):
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "Selected folder does not exist.")
        return

    os.makedirs("logs", exist_ok=True)
    log_path = os.path.join("logs", "run_log.txt")

    with open(log_path, "a") as log_file:
        log_file.write(f"\nRun at {datetime.now()}\n")
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                ext = os.path.splitext(filename)[1].lower()
                folder_name = EXTENSION_MAP.get(ext, 'Others')
                target_folder = os.path.join(folder_path, folder_name)
                os.makedirs(target_folder, exist_ok=True)
                new_path = os.path.join(target_folder, filename)
                shutil.move(file_path, new_path)
                log_file.write(f"Moved: {filename} -> {folder_name}\n")

    status_label.config(text="Files organized successfully!", fg="green")
    messagebox.showinfo("Done", "Files have been organized.")

def browse_folder(entry_field):
    folder_selected = filedialog.askdirectory()
    if folder_selected:
        entry_field.delete(0, tk.END)
        entry_field.insert(0, folder_selected)

def create_gui():
    root = tk.Tk()
    root.title("File Organizer Tool")
    root.geometry("450x200")
    root.resizable(False, False)

    tk.Label(root, text="Select Folder to Organize:", font=("Arial", 12)).pack(pady=10)

    entry = tk.Entry(root, width=50)
    entry.pack(pady=5)

    browse_btn = tk.Button(root, text="Browse", command=lambda: browse_folder(entry))
    browse_btn.pack()

    status_label = tk.Label(root, text="", fg="blue")
    status_label.pack(pady=10)

    organize_btn = tk.Button(
        root, text="Organize Files",
        command=lambda: organize_files(entry.get(), status_label),
        bg="#4CAF50", fg="white", padx=10, pady=5
    )
    organize_btn.pack()

    root.mainloop()

if __name__ == "__main__":
    create_gui()


print("Press any button to exit")
input()
