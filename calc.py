import tkinter as tk

light_gray = "#F5F5F5"
class Calculator:
    def __init__(self) -> None:
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.display_frame = self.create_display_frame()
        self.button_frame = self.create_buttons_frame()
    
    def run(self):
        self.window.mainloop()

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