import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        # Create the display widget
        self.display = tk.Entry(master, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Create the buttons
        self.button_1 = tk.Button(master, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = tk.Button(master, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = tk.Button(master, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = tk.Button(master, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = tk.Button(master, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = tk.Button(master, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = tk.Button(master, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = tk.Button(master, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = tk.Button(master, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = tk.Button(master, text="0", padx=40, pady=20, command=lambda: self.button_click(0))

        self.button_add = tk.Button(master, text="+", padx=38.5, pady=20, command=self.button_add)
        self.button_subtract = tk.Button(master, text="-", padx=41, pady=20, command=self.button_subtract)
        self.button_multiply = tk.Button(master, text="*", padx=41, pady=20, command=self.button_multiply)
        self.button_divide = tk.Button(master, text="/", padx=41, pady=20, command=self.button_divide)

        self.button_clear = tk.Button(master, text="Clear", padx=29, pady=20, command=self.button_clear)
        self.button_square = tk.Button(master, text="square", padx=25, pady=20, command=self.button_square)
        self.button_equals = tk.Button(master, text="=", padx=184.2, pady=20, command=self.button_equals)

        # Put the buttons on the screen
        self.button_1.grid(row=1, column=0)
        self.button_2.grid(row=1, column=1)
        self.button_3.grid(row=1, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_7.grid(row=3, column=0)
        self.button_8.grid(row=3, column=1)
        self.button_9.grid(row=3, column=2)

        self.button_0.grid(row=4, column=0)

        self.button_add.grid(row=1, column=3)
        self.button_subtract.grid(row=2, column=3)
        self.button_multiply.grid(row=3, column=3)
        self.button_divide.grid(row=4, column=3)

        self.button_clear.grid(row=4, column=1 )
        self.button_square.grid(row=4, column=2)
        self.button_equals.grid(row=5, column=0, columnspan=4)

        # Initialize the calculator state
        self.current_value = 0
        self.operation = None
        self.clear_display = False

    def button_click(self, number):
        if self.clear_display:
            self.display.delete(0, tk.END)
            self.clear_display = False
        self.display.insert(tk.END, number)

    def button_clear(self):
        self.display.delete(0, tk.END)

    def button_add(self):
        self.operation = "+"
        self.current_value = int(self.display.get())
        self.clear_display = True

    def button_subtract(self):
        self.operation = "-"
        self.current_value = int(self.display.get())
        self.clear_display = True

    def button_multiply(self):
        self.operation = "*"
        self.current_value = int(self.display.get())
        self.clear_display = True

    def button_divide(self):
        self.operation = "/"
        self.current_value = int(self.display.get())
        self.clear_display = True

    def button_square(self):
        self.operation = "**"
        self.current_value = int(self.display.get())
        self.clear_display = True
    def button_equals(self):
        if self.operation:
            second_value = int(self.display.get())
            if self.operation == "+":
                result = self.current_value + second_value
            elif self.operation == "-":
                result = self.current_value - second_value
            elif self.operation == "*":
                result = self.current_value * second_value
            elif self.operation == "**":
                result = self.current_value ** 2
            else:
                result = self.current_value / second_value
            self.display.delete(0, tk.END)
            self.display.insert(0, result)
            self.operation = None
            self.current_value = 0
            self.clear_display = True

root = tk.Tk()
calc = Calculator(root)
root.mainloop()
