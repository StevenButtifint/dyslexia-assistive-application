import pyglet

from res.constants import *
from res.interface import *


class Window:
    def __init__(self, parent):
        self.window = parent
        self.window.resizable(0, 0)
        self.window.geometry(HOME_DIMENSIONS)
        self.window.title(APP_TITLE)
        self.window.iconbitmap(self.resource_path(APP_ICON_DIR))
        self.window_opaque = True
        self._create_tool_bar()

    def _create_tool_bar(self):
        toolbar_frame = make_static_frame(self.window, TOOLBAR_BG, 2000, 85, 0, 0, "nw")
        self.home_tool = make_tool_button(toolbar_frame, 50, 50, 1, 1, lambda: self._create_home_page(), HOME_ICON_DIR)
        self.colour_overlay = make_tool_button(toolbar_frame, 50, 50, 55, 1, lambda: self._colour_overlay(), OVERLAY_ICON_DIR)
        self.notice_frame = make_static_frame(toolbar_frame, NOTICE_BG, 2000, 25, 0, 50, "nw")
        self.notice_label = make_label(self.notice_frame, HOME_NOTICE, NOTICE_BG, NOTICE_TEXT, 5, 0, "nw", 12)
        self.options_frame = make_static_frame(self.window, "black", 600, 5, 0, 85, "nw")
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

    def _set_overlay_colour(self, index):
        colour = OVERLAY_COLOURS[index]
        self.options_frame.config(bg=colour)
        self.alpha_scale.config(bg=colour, troughcolor=colour)
        self.alpha_label.config(bg=colour)
        self.toggle_label.config(bg=colour)
        self.colours_label.config(bg=colour)
        if self.window_opaque:
            self.alpha_toggle.config(bg=colour)

    def _toggle_window_opaque(self, is_toggle):
        if is_toggle:
            if self.window_opaque:
                self.window.attributes('-alpha', self.alpha_scale.get() / 100)
                self.alpha_toggle.config(bg="green")
                self.window_opaque = False
            else:
                self.alpha_toggle.config(bg=self.options_frame["background"])
                self.window.attributes('-alpha', 1)
                self.window_opaque = True
        else:
            self.alpha_label.config(text="Opacity: "+str(self.alpha_scale.get())+"%")
            if not self.window_opaque:
                self.window.attributes('-alpha', self.alpha_scale.get() / 100)

    def _reading_editor(self):
        self._tool_selected(self.reading_editor)
        self.notice_label.config(text=READING_EDITOR_NOTICE)
        self.options_frame.destroy()
        self.options_frame = make_static_frame(self.window, MAIN_BG, 1600, 1000, 0, 75, "nw")
        self.window.geometry(READING_DIMENSIONS)

        pyglet.font.add_file(DYSLEXIC_FONT_DIR)
        self.text_box_size = 20
        text_font = ("OpenDyslexic-Regular", self.text_box_size)
        self.text_box_frame = make_static_frame(self.options_frame, "red", 1560, 800, 20, 100, "nw")
        self.text_box = make_scaling_text_box(self.text_box_frame, OVERLAY_COLOURS[0], "black", 0, 0, text_font)


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
