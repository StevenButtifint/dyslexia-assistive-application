
from res.constants import *
from res.interface import *


class Window:
    def __init__(self, parent):
        self.window = parent
        self.window.resizable(0, 0)
        self.window.geometry(HOME_DIMENSIONS)
        self.window.title(APP_TITLE)


if __name__ == "__main__":
    root = tk.Tk()
    Window(root)
    root.mainloop()
