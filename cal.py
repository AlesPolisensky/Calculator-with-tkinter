import tkinter as tk

GRAY = "#F5F5F5"
LABEL_COLOR = "#000000"
SMALL_FONT = ("Arial", 16)
LARGE_FONT = ("Arial", 40, "bold")
WHITE = "#FFFFFF"
DIGIT_FONT = ("Arial", 24, "bold")
DEFAULT_FONT = ("Arial", 20)
OFF_WHITE = "#F8FAFF"
BLUE = "#CCEDFF"


class Calc:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Simple Calculator")
        self.display_frame = self.create_display()
        self.button_frame = self.create_button()
        self.total = ""
        self.curr = ""

        self.total_label, self.curr_label = self.create_display_labl()
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 1), ".": (4, 2)
        }
        self.create_digit_buttons()
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.create_operator_buttons()
        self.create_special_buttons()
        
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)
        self.bind_keys()
            
    def pow(self):
        self.curr = str(eval(f"{self.curr}**2"))
        self.update_curr() 
        
    def sqrt(self):
        self.curr = str(eval(f"{self.curr}**0.5"))
        self.update_curr() 
            
    def evaluate(self):
        self.total += self.curr
        self.update_total()
        
        try:
            self.curr = str(eval(self.total))
            self.total= ""
        except Exception as e:
            self.curr = "Error"
        finally:
            self.update_curr()
            
    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))
                         
    def clear(self):
        self.curr = ""
        self.total = ""
        self.update_curr()
        self.update_total()
               
    def append_operator(self, operator):
        self.curr += operator
        self.total += self.curr
        self.curr = ""
        self.update_total()
        self.update_curr()
        
            
    def update_total(self):
        expression = self.total
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.total_label.config(text=expression)
    
    def update_curr(self):
        self.curr_label.config(text=self.curr[:11])
        
    def add_to(self, value):
        self.curr += str(value)
        self.update_curr()     
                
    def create_special_buttons(self):
        self.create_C_button()
        self.create_equals_button()
        self.create_sqrt_button()
        self.create_power_button()

    def create_C_button(self):
        button = tk.Button(self.button_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)
        
    def create_power_button(self):
        button = tk.Button(self.button_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=self.pow)
        button.grid(row=0, column=2, sticky=tk.NSEW)
        
    def create_sqrt_button(self):
        button = tk.Button(self.button_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=", bg=BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT,
                               borderwidth=0, command=lambda x=digit: self.add_to(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_display_labl(self):
        total_label = tk.Label(self.display_frame, text=self.total, anchor=tk.E,
                               bg=GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT)
        total_label.pack(expand=True, fill="both")

        curr_label = tk.Label(self.display_frame, text=self.curr, anchor=tk.E,
                              bg=GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT)
        curr_label.pack(expand=True, fill="both")

        return total_label, curr_label

    def create_display(self):
        frame = tk.Frame(self.window, height=221, bg=GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def create_button(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    Calc().run()
