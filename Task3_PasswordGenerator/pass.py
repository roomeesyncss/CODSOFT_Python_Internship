import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip
from ttkbootstrap import Style


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x200')
        self.root.title("Password Generator")

        self.style = Style('darkly')

        self.create_widgets()

    def create_widgets(self):
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)

        self.length_label = ttk.Label(self.root, text="Password Length:")
        self.length_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.length_entry = ttk.Entry(self.root, width=5)
        self.length_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)

        self.special_var = tk.BooleanVar(value=True)
        self.special_checkbox = ttk.Checkbutton(self.root, text="Include Special Characters", variable=self.special_var)
        self.special_checkbox.grid(row=1, column=0, columnspan=2, pady=(0, 10), sticky=tk.W)

        self.generate_button = ttk.Button(self.root, text="Generate Password", command=self.generate_password,
                                          style='primary.TButton')
        self.generate_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.result_label = ttk.Label(self.root, text="Generated Password:")
        self.result_label.grid(row=3, column=0, padx=10, pady=(10, 5), sticky=tk.W)

        self.result_entry = ttk.Entry(self.root, width=20, state=tk.DISABLED)
        self.result_entry.grid(row=3, column=1, padx=10, pady=(10, 5), sticky=tk.W)

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            if length < 1:
                messagebox.showwarning("Invalid Length", "Password length must be at least 1.")
                return

            password = self._generate_password(length, self.special_var.get())
            self.result_entry.config(state=tk.NORMAL)
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, password)
            self.result_entry.config(state=tk.DISABLED)

            # Copy the generated password to the clipboard
            pyperclip.copy(password)

            messagebox.showinfo("Password Copied", "Generated password copied to clipboard.")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number for password length.")

    def _generate_password(self, length, include_special):
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation if include_special else ''

        all_characters = lowercase_letters + uppercase_letters + digits + special_characters

        if length < 8:
            length = 8

        password = ''.join(random.choice(all_characters) for _ in range(length))
        return password


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
