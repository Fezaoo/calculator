import tkinter as tk

small_font_style = ("Arial", 16)
light_gray = "#F5F5F5"
label_color = "#25265E"
class Calculator:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = "0"
        self.current_expression = "0"
        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_buttons_frame()
    
    def run(self):
        self.window.mainloop()

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=light_gray, fg=label_color, padx=24, font=small_font_style)
        total_label.pack(expand=True, fill="both")

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=225, bg=light_gray)
        frame.pack(expand=True, fill="both")
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

if True:
    calc = Calculator()
    calc.run()