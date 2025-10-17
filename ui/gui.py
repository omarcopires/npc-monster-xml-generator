import os
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from tkinter import PhotoImage
import webbrowser
from core import processor

def run_gui():
    # Create main window
    root = tk.Tk()
    root.title("NPC & Monster XML Generator")
    root.geometry("540x300")
    root.configure(bg="#121212")
    root.resizable(False, False)
    root.eval('tk::PlaceWindow . center')
    icon = PhotoImage(file="icon.png")
    root.iconphoto(True, icon)

    # Styles
    style = ttk.Style()
    style.theme_use("clam")

    PRIMARY = "#0d6efd"
    PRIMARY_HOVER = "#0b5ed7"
    BG = "#121212"
    FG = "#e0e0e0"
    INPUT_BG = "#1e1e1e"

    style.configure("TFrame", background=BG)
    style.configure("TLabel", background=BG, foreground=FG, font=('Segoe UI', 10))
    style.configure("Title.TLabel", font=('Segoe UI', 14, 'bold'), foreground="#ffffff", background=BG)
    style.configure("TEntry", fieldbackground=INPUT_BG, foreground=FG, insertcolor=FG, borderwidth=1, relief="flat", padding=5)
    style.configure("TButton", font=('Segoe UI', 10, 'bold'), borderwidth=0, padding=6)
    style.map("TButton", background=[("active", PRIMARY_HOVER)])
    style.configure("Primary.TButton", background=PRIMARY, foreground="#ffffff")

    # Header
    ttk.Label(root, text="🧩 NPC & Monster XML Generator", style="Title.TLabel").pack(pady=15)

    # Folder selection
    frame = ttk.Frame(root)
    frame.pack(pady=5)
    path_var = tk.StringVar()
    entry = ttk.Entry(frame, textvariable=path_var, width=50)
    entry.pack(side=tk.LEFT, padx=5)

    def select_folder():
        folder = filedialog.askdirectory(title="Select folder with Lua files")
        if folder:
            path_var.set(folder)

    ttk.Button(frame, text="📂 Browse", style="Primary.TButton", command=select_folder).pack(side=tk.LEFT)

    # Progress bar
    progress = ttk.Progressbar(root, length=320)
    progress.pack(pady=5)

    # Status label
    status_var = tk.StringVar(value="Waiting for input...")
    status_label = ttk.Label(root, textvariable=status_var, foreground="#ccc", font=('Segoe UI', 9), background=BG)
    status_label.pack(pady=2)

    # Footer with GitHub link
    def open_github(event=None):
        webbrowser.open_new("https://github.com/omarcopires")

    footer = tk.Label(
        root,
        text="© 2025 - Developed by @omarcopires",
        bg=BG,
        fg="#999",
        cursor="hand2",
        font=('Segoe UI', 9, 'underline')
    )
    footer.pack(side=tk.BOTTOM, pady=8)
    footer.bind("<Button-1>", open_github)

    # Generate button
    def run():
        folder = path_var.get().strip()
        if not folder or not os.path.isdir(folder):
            messagebox.showerror("Error", "Please select a valid folder containing Lua files.")
            return

        # Detect type automatically
        type_ = processor.detect_type(folder)

        # Project root directory
        project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

        # Create output folder if it doesn't exist
        output_dir = os.path.join(project_root, "output")
        os.makedirs(output_dir, exist_ok=True)

        # Full path for the XML file
        output_file = os.path.join(output_dir, f"{type_}.xml")

        # Disable button and reset progress
        btn_generate.config(state='disabled')
        progress["value"] = 0
        progress["maximum"] = 100

        # Update progress bar
        def update_progress(current, total):
            value = int((current / total) * 100)
            progress["value"] = value
            status_var.set(f"Processing {current} of {total} files...")
            root.update_idletasks()

        # Generate XML
        def generate():
            try:
                success, skipped = processor.process_files(folder, output_file, update_progress, type_=type_)
                status_var.set("Completed!")
                messagebox.showinfo(
                    "Success",
                    f"✅ {type_.capitalize()} processed: {success}\n🚫 Files skipped: {skipped}\n\n📄 XML saved at:\n{output_file}"
                )
            except Exception as e:
                messagebox.showerror("Error", str(e))
            finally:
                btn_generate.config(state='normal')
                progress["value"] = 100

        root.after(100, generate)

    # Create generate button
    btn_generate = ttk.Button(root, text="🚀 Generate XML", style="Primary.TButton", command=run)
    btn_generate.pack(pady=15)

    # Start main loop
    root.mainloop()
