import tkinter as tk
from pynput.mouse import Listener as MouseListener
import time
from tkinter import messagebox
from show_alert import show_alert


class App:
    def __init__(self, root):
        self.root = root
        root.title("Label text change sample")
        root.geometry("500x500")
        self.label = tk.Label(root, text="")
        self.label.pack()

        self.mouse_listener = MouseListener(
            on_move=self.move, on_click=self.click, on_scroll=self.scroll)
        self.mouse_listener.start()

        self.timer_start = time.time()
        self.timer = self.timer_start
        self.alert_timer = None

        root.mainloop()

    def move(self, x, y):
        self.change()

    def click(self, x, y, button, pressed):
        self.change()

    def scroll(self, x, y, dx, dy):
        self.change()

    def change(self):
        self.timer = time.time()
        elapsed_time = self.timer - self.timer_start
        self.label["text"] = f"{elapsed_time}"

        if self.alert_timer:
            self.root.after_cancel(self.alert_timer)

        self.alert_timer = self.root.after(3000, show_alert)



def main():
    root = tk.Tk()
    app = App(root)


if __name__ == "__main__":
    main()
