import tkinter as tk
from tkinter import ttk
import math

# Define the calculator class
class ScientificCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.root.geometry("400x400")

        self.expression = ""
        self.text_input = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):

        # Data Entry box
        entry = tk.Entry(
            self.root,
            textvariable=self.text_input,
            font=('arial', 20, 'bold'),
            justify='right'
        )
        entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),

            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),

            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),

            ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),

            ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('^', 5, 3),

            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),

            ('sqrt', 7, 0), ('exp', 7, 1), ('pi', 7, 2), ('e', 7, 3)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    # Create buttons
    def create_button(self, text, row, col):

        button = ttk.Button(
            self.root,
            text=text,
            command=lambda: self.on_button_click(text)
        )

        button.grid(row=row, column=col, sticky='nsew')

    # Button click function
    def on_button_click(self, char):

        if char == 'C':
            self.expression = ""

        elif char == '=':
            self.calculate_result()
            return

        elif char == 'pi':
            self.expression += str(math.pi)

        elif char == 'e':
            self.expression += str(math.e)

        elif char == 'sqrt':
            self.expression += 'math.sqrt('

        elif char == 'sin':
            self.expression += 'math.sin(math.radians('

        elif char == 'cos':
            self.expression += 'math.cos(math.radians('

        elif char == 'tan':
            self.expression += 'math.tan(math.radians('

        elif char == 'log':
            self.expression += 'math.log10('

        elif char == 'exp':
            self.expression += 'math.exp('

        elif char == '^':
            self.expression += '**'

        else:
            self.expression += str(char)

        self.text_input.set(self.expression)

    # Calculate result
    def calculate_result(self):

        try:
            result = eval(
                self.expression,
                {"__builtins__": {}},
                {"math": math}
            )

            self.text_input.set(str(result))
            self.expression = str(result)

        except Exception:
            self.text_input.set("Error")
            self.expression = ""


# Main function
def main():

    root = tk.Tk()

    calculate = ScientificCalculator(root)

    root.mainloop()


if __name__ == "__main__":
    main()