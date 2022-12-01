
from res.constants import *
from res.interface import *


class Window:
    def __init__(self, parent):
        self.window = parent
        self.window.resizable(0, 0)
        self.window.geometry(HOME_DIMENSIONS)
        self.window.title(APP_TITLE)
        self.window.iconbitmap(self.resource_path(APP_ICON_DIR))
        self._create_tool_bar()

    def _create_tool_bar(self):
        toolbar_frame = make_static_frame(self.window, TOOLBAR_BG, 2000, 85, 0, 0, "nw")
        self.home_tool = make_tool_button(toolbar_frame, 50, 50, 1, 1, lambda: self._create_home_page(), HOME_ICON_DIR)
        self.tool_selected = self.home_tool
        self.home_tool.config(bg=TOOL_BG_CLICKED)

    def _create_home_page(self):
        self._tool_selected(self.home_tool)
        self.notice_label.config(text=HOME_NOTICE)
        self.window.geometry(HOME_DIMENSIONS)
        self.options_frame.destroy()
        self.options_frame = make_static_frame(self.window, "red", 600, 25, 0, 75, "nw")

    def _colour_overlay(self):
        self._tool_selected(self.colour_overlay)
        self.notice_label.config(text=COLOUR_OVERLAY_NOTICE)
        self.options_frame.destroy()
        self.window_opaque = True
        self.options_frame = make_static_frame(self.window, OVERLAY_COLOURS[0], 2000, 1500, 0, 75, "nw")

    def _tool_selected(self, tool_button):
        self.window.attributes('-alpha', 1)
        if self.tool_selected is not tool_button:
            self.tool_selected.config(bg=TOOL_BG)
        self.tool_selected = tool_button

    @staticmethod
    def resource_path(relative_path):
        # res path based on running local or deployed version
        try:
            base_path = sys._MEIPASS
        except Exception:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    root = tk.Tk()
    Window(root)
    root.mainloop()
