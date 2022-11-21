from res.interface import *


class Window:
    def __init__(self, parent):
        self.window = parent


if __name__ == "__main__":
    root = tk.Tk()
    Window(root)
    root.mainloop()
