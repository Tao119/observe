from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Listener as KeyboardListener
import tkinter as tk


class App:
    def __init__(self,root):
        self.root = root
        root.title("Label text change sample")
        root.geometry("500x500")
        self.keyboard_listener = KeyboardListener(
            on_press=self.on_press, on_release=self.on_release)
        self.mouse_listener = MouseListener(
            on_move=self.on_move, on_click=self.on_click, on_scroll=self.on_scroll)

        self.keyboard_listener.start()
        self.mouse_listener.start()
        root.mainloop()

    def on_press(self, key):
        print("Key pressed: {0}".format(key))

    def on_release(self, key):
        print("Key released: {0}".format(key))

    def on_move(self, x, y):
        print("Mouse moved to ({0}, {1})".format(x, y))

    def on_click(self, x, y, button, pressed):
        if pressed:
            print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        else:
            print('Mouse released at ({0}, {1}) with {2}'.format(x, y, button))

    def on_scroll(self, x, y, dx, dy):
        print('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))


def main():
    root = tk.Tk()
    app = App(root)


if __name__ == "__main__":
    main()
