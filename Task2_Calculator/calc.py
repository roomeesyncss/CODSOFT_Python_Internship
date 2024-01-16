import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry('300x400')
        self.root.title("Calculator")

        self.style = Style('darkly')
        self.resulted = ""

        self.create_widgets()

    def create_widgets(self):
        self.text_result = tk.Text(
            self.root,
            height=2,
            width=17,
            font=("Helvetica", 20),
            bg="#cbced4",
            fg="#676f82",
            bd=5,
            relief=tk.FLAT
        )
        self.text_result.grid(
            row=0,
            column=0,
            columnspan=4,
            pady=(10, 0),
            padx=10
        )

        self.create_number_buttons()
        self.create_operator_buttons()

        ttk.Button(
            self.root,
            text="(",
            command=lambda: self.add_to_calculation("("),
            width=5,
            style='secondary.TButton'
        ).grid(row=5, column=0)

        ttk.Button(
            self.root,
            text=")",
            command=lambda: self.add_to_calculation(")"),
            width=5,
            style='secondary.TButton'
        ).grid(row=5, column=2)

        ttk.Button(
            self.root,
            text="C",
            command=self.clear_field,
            width=11,
            style='danger.TButton'
        ).grid(row=6, column=0, columnspan=2, sticky="nsew")

        ttk.Button(
            self.root,
            text="=",
            command=self.evaluate_calculation,
            width=11,
            style='success.TButton'
        ).grid(row=6, column=2, columnspan=2, sticky="nsew")

        for i in range(7):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def create_number_buttons(self):
        for i in range(1, 10):
            ttk.Button(
                self.root,
                text=str(i),
                command=lambda i=i: self.add_to_calculation(i),
                width=5,
                style='primary.TButton'
            ).grid(row=2 + (i - 1) // 3, column=(i - 1) % 3)

        ttk.Button(
            self.root,
            text="0",
            command=lambda: self.add_to_calculation(0),
            width=5,
            style='primary.TButton'
        ).grid(row=5, column=1)

    def create_operator_buttons(self):
        operators = ["+", "-", "*", "/"]
        for i, operator in enumerate(operators):
            ttk.Button(
                self.root,
                text=operator,
                command=lambda operator=operator: self.add_to_calculation(operator),
                width=5,
                style='secondary.TButton'
            ).grid(row=2 + i, column=3)

    def add_to_calculation(self, symbol):
        self.resulted += str(symbol)
        self.update_display()

    def evaluate_calculation(self):
        try:
            self.resulted = str(eval(self.resulted))
            self.update_display()
        except Exception as e:
            self.clear_field()
            self.text_result.insert(1.0, "Error")

    def clear_field(self):
        self.resulted = ""
        self.update_display()

    def update_display(self):
        self.text_result.delete(1.0, "end")
        self.text_result.insert(1.0, self.resulted)


if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
