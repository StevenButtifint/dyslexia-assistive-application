
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
        self.toggle_label = make_label(self.options_frame, "Toggle overlay", OVERLAY_COLOURS[0], "black", 72, 20, "center", 12)
        self.toggle_label.config(font=font.Font(slant="italic"))
        self.alpha_scale = makeScale(self.options_frame, 20, 90, 225, 26+19, 22, 160, OVERLAY_COLOURS[0], "blue", lambda _=None: self._toggle_window_opaque(False))
        self.alpha_scale.config(showvalue=0, troughcolor=OVERLAY_COLOURS[0])
        self.alpha_label = make_label(self.options_frame, "Opacity: 20%", OVERLAY_COLOURS[0], "black", 175, 8, "nw", 12)
        self.alpha_label.config(font=font.Font(slant="italic"))
        self.alpha_toggle = make_img_button(self.options_frame, "", 20, 100, OVERLAY_COLOURS[0], "black", 72, 26+19, lambda: self._toggle_window_opaque(True), 0, POWER_ICON_DIR)

        self.colours_label = make_label(self.options_frame, "Background Colour", OVERLAY_COLOURS[0], "black", 505, 20, "center", 12)
        self.colours_label.config(font=font.Font(slant="italic"))

        self.colour_buttons = []
        for x in range(0, len(OVERLAY_COLOURS)):
            self.colour_buttons.append(make_button(self.options_frame, "", 11, 16, OVERLAY_COLOURS[x], "black", 340+(30*x), 26+19, lambda c=x: self._set_overlay_colour(c), 1))

        self.window.geometry(OVERLAY_DIMENSIONS)


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
