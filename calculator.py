import tkinter as tk

LIGHT_BLUE = '#CCEDFF'
LIGHT_GRAY = '#F5F5F5'
DEFAULT_FONT_STYLE = ('Arial', 20)
OFF_WHITE = '#F8FAFF'
LABEL_COLOR = '#25265E'
SMALL_FONT_STYLE = ('Arial', 16)
LARGE_FONT_STYLE = ('Arial', 40, 'bold')
DIGIT_FONT_STYLE = ('Arial', 24, 'bold')


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('375x667')
        self.window.resizable(0, 0)
        self.window.title('Calculator')
        self.operations = {'/': '\u00F7', '*': '\u00D7', '-': '-', '+': '+'}
        self.total_expression = ''
        self.current_expression = ''
        self.display_frame = self.create_display_frame()

        self.total_label = self.create_display_labels()
        self.label = self.create_display_labels()
        self.buttons_frame = self.create_buttons_frame()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),  # row 1
            4: (2, 1), 5: (2, 2), 6: (2, 3),  # row 2
            1: (3, 1), 2: (3, 2), 3: (3, 3),  # row 3
            '.': (4, 1), 0: (4, 2)   # row 4
        }

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE,
                               fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text='C', bg=OFF_WHITE,
                           fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', bg=LIGHT_BLUE,
                           fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE, borderwidth=0)
        button.grid(row=4, column=3, columnspan=2,
                    sticky=tk.NSEW)

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(
                digit), bg='White', fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda: self.add_to_expression(digit))
            button.grid(row=grid_value[0],
                        column=grid_value[1], sticky=tk.NSEW)

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression,
                               anchor=tk.E,  bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.total_expression,
                         anchor=tk.E,  bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        self.label.config(text=self.current_expression)

    def run(self):
        self.window.mainloop()


calc = Calculator()
calc.run()
