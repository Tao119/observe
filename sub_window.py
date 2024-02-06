import tkinter as tk
import tkinter.ttk as ttk

def sub_window():
    sub_win = tk.Toplevel()
    sub_win.geometry("300x100")
    label_sub = tk.Label(sub_win, text="サブウィンドウ")
    label_sub.pack()
