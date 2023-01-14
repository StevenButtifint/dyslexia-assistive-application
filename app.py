import pyglet
import os
from gtts import gTTS

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

        self.text_box_size = 20
        pyglet.font.add_file(DYSLEXIC_FONT_DIR)
        self.text_font = ("OpenDyslexic-Regular", self.text_box_size)

        self._create_tool_bar()

    def _create_tool_bar(self):
        toolbar_frame = make_static_frame(self.window, TOOLBAR_BG, 2000, 85, 0, 0, "nw")
        self.home_tool = make_tool_button(toolbar_frame, 50, 50, 1, 1, lambda: self._create_home_page(), HOME_ICON_DIR)
        self.colour_overlay = make_tool_button(toolbar_frame, 50, 50, 55, 1, lambda: self._colour_overlay(), OVERLAY_ICON_DIR)
        self.reading_editor = make_tool_button(toolbar_frame, 50, 50, 109, 1, lambda: self._reading_editor(), READING_ICON_DIR)
        self.spellchecker = make_tool_button(toolbar_frame, 50, 50, 163, 1, lambda: self._spellchecker(), SPELLCHECKER_ICON_DIR)

        self.text_reader = make_tool_button(toolbar_frame, 50, 50, 217, 1, lambda: self._text_speaker(), TTS_ICON_DIR)  # text to speech

        self.info = make_tool_button(toolbar_frame, 50, 50, 487, 1, lambda: self._info(), INFO_ICON_DIR)
        self.exit = make_tool_button(toolbar_frame, 50, 50, 544, 1, lambda: self._exit(), EXIT_ICON_DIR)

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
        self.options_frame = make_static_frame(self.window, MAIN_BG, 600, 25, 0, 75, "nw")

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

        self.text_box_frame = make_static_frame(self.options_frame, MAIN_BG, 1560, 800, 20, 100, "nw")
        self.text_box = make_scaling_text_box(self.text_box_frame, OVERLAY_COLOURS[0], "black", 0, 0, self.text_font)

        self._create_textbox_size_options()


        text_font_label = make_label(self.options_frame, "Text font", MAIN_BG, "black", 532, 20, "center", 12)
        text_font_label.config(font=font.Font(slant="italic"))

        make_option_menu(self.options_frame, CUSTOM_FONTS, 0, 532, 47, "center", MAIN_BG)


    def _create_textbox_fg_options(self):
        self.greyscale_buttons = []
        self.selected_fg_colour = 0

        for x in range(0, len(GREYSCALE_COLOURS), 2):
            self.greyscale_buttons.append(make_button(self.options_frame, "", 11, 16, GREYSCALE_COLOURS[x], "black", 160+(15*x), 26+19, lambda c=x: self._set_text_colour(self.text_box, c), 1))
            self.greyscale_buttons.append(make_button(self.options_frame, "", 11, 16, GREYSCALE_COLOURS[x+1], "black", 160+(15*x), 53+19, lambda c=x: self._set_text_colour(self.text_box, c+1), 1))

        text_colour_label = make_label(self.options_frame, "Text colour", MAIN_BG, "black", 190, 20, "center", 12)
        text_colour_label.config(font=font.Font(slant="italic"))

    def _create_textbox_bg_options(self):
        self.colour_buttons = []
        self.selected_bg_colour = 0

        for x in range(0, len(OVERLAY_COLOURS), 2):
            self.colour_buttons.append(make_button(self.options_frame, "", 11, 16, OVERLAY_COLOURS[x], "black", 250+(15*x)+18, 26+19, lambda c=x: self._set_text_box_colour(c), 1))
            self.colour_buttons.append(make_button(self.options_frame, "", 11, 16, OVERLAY_COLOURS[x+1], "black", 250+(15*x)+18, 53+19, lambda c=x: self._set_text_box_colour(c+1), 1))

        bg_colour_label = make_label(self.options_frame, "Background colour", MAIN_BG, "black", 345, 20, "center", 12)
        bg_colour_label.config(font=font.Font(slant="italic"))

    def _create_textbox_size_options(self):
        make_img_button(self.options_frame, "", 48, 48, MAIN_BG, "black", 46, 40+19, lambda: self._set_text_box_size(2), 0, ZOOM_IN_ICON_DIR)
        make_img_button(self.options_frame, "", 48, 48, MAIN_BG, "black", 102, 40+19, lambda: self._set_text_box_size(-2), 0, ZOOM_OUT_ICON_DIR)
        text_size_label = make_label(self.options_frame, "Text size", MAIN_BG, "black", 72, 20, "center", 12)
        text_size_label.config(font=font.Font(slant="italic"))

    def _spellchecker(self):
        self._tool_selected(self.spellchecker)
        self.notice_label.config(text=SPELLCHECKER_NOTICE)
        self.options_frame.destroy()
        self.options_frame = make_static_frame(self.window, MAIN_BG, 800, 1000, 0, 75, "nw")
        self.window.geometry(SPELLCHECKER_DIMENSIONS)


    def _text_speaker(self):
        self._tool_selected(self.text_reader)
        self.notice_label.config(text=TEXT_SPEAKER_NOTICE)
        self.options_frame.destroy()
        self.options_frame = make_static_frame(self.window, MAIN_BG, 1600, 1000, 0, 75, "nw")
        self.window.geometry(TEXT_SPEAKER_DIMENSIONS)

        text_box_frame = make_static_frame(self.options_frame, MAIN_BG, 560, 600, 18, 100, "nw")
        self.text_box = make_scaling_text_box(text_box_frame, OVERLAY_COLOURS[0], "black", 0, 0, self.text_font)


        make_img_button(self.options_frame, "", 64, 64, MAIN_BG, "black", 280, 760, lambda: self._speak_text(self.text_box.get("1.0", tk.END)), 0, VOICE_ICON_DIR)

    @staticmethod
    def _speak_text(text):
        audio = gTTS(text=text, lang="en", slow=False)
        audio.save("tts.mp3")
        os.system("start tts.mp3")

    def _info(self):
        self._tool_selected(self.info)
        self.notice_label.config(text=INFO_NOTICE)
        self.options_frame.destroy()
        self.options_frame = make_static_frame(self.window, MAIN_BG, 1600, 1000, 0, 75, "nw")
        self.window.geometry(INFO_DIMENSIONS)

    def _exit(self):
        self._tool_selected(self.exit)
        self.notice_label.config(text=" "*45 + EXIT_NOTICE)
        self.options_frame.destroy()
        self.options_frame = make_static_frame(self.window, NOTICE_BG, 1600, 1000, 0, 75, "nw")
        self.window.geometry(EXIT_DIMENSIONS)
        make_button(self.options_frame, "Yes", 1, 4, MAIN_BG, "black", 250, 25, lambda: quit(), 16)
        make_button(self.options_frame, "No", 1, 4, MAIN_BG, "black", 340, 25, lambda: self._cancel_exit(), 16)

    def _cancel_exit(self):
        self.home_tool.config(bg=TOOL_BG_CLICKED)
        self._create_home_page()

    def _set_text_box_size(self, increment):
        self.text_box_size = self.text_box_size+increment
        self.text_box.config(font=("OpenDyslexic-Regular", self.text_box_size))

    def _set_text_box_colour(self, colour):
        self.colour_buttons[self.selected_bg_colour].config(borderwidth=1)
        self.selected_bg_colour = colour
        self.text_box.config(bg=OVERLAY_COLOURS[colour])

    def _set_text_colour(self, box, colour):
        self.greyscale_buttons[self.selected_fg_colour].config(borderwidth=2)
        self.selected_fg_colour = colour
        box.config(fg=GREYSCALE_COLOURS[colour])

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
