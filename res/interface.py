import os
import tkinter as tk
import tkinter.font as font

from PIL import Image, ImageTk

from res.constants import *


def make_static_frame(frame, bg, w, h, x, y, anchor):
    new_frame = tk.Frame(frame, bg=bg)
    new_frame.place(width=w, height=h, x=x, y=y, anchor=anchor)
    return new_frame


def make_label(frame, text, bg, fg, x, y, anchor, size):
    label = tk.Label(frame, text=text, bg=bg, fg=fg)
    label.place(x=x, y=y, anchor=anchor)
    label['font'] = font.Font(family='Helvetica', size=size)
    return label


def make_option_menu(frame, options, default_idx, x, y, anchor, bg):
    string_var = tk.StringVar(frame)
    string_var.set(options[default_idx])
    option_menu = tk.OptionMenu(frame, string_var, *options)
    option_menu.config(bg=bg)
    option_menu["menu"].config(bg=bg)
    option_menu["highlightthickness"]=0
    # option_menu.config(bg=bg, highlightthickness=0, activebackground=BUTTON_BG_HOVER)
    # option_menu["menu"].config(borderwidth=0, bg=bg)
    option_menu["borderwidth"]=1
    option_menu.place(x=x, y=y, anchor=anchor)
    return option_menu


def mouse_enter_tool(e):
    if e.widget['background'] != TOOL_BG_CLICKED:
        e.widget['background'] = TOOL_BG_HOVER


def mouse_leave_tool(e):
    if e.widget['background'] != TOOL_BG_CLICKED:
        e.widget['background'] = TOOL_BG


def mouse_release_tool(e):
    e.widget['background'] = TOOL_BG_CLICKED


def mouse_enter_tile(e):
    e.widget.config(borderwidth=3)


def mouse_leave_tile(e):
    e.widget.config(borderwidth=1)


def make_tool_button(frame, height, width, x, y, command, image_dir):
    image = Image.open(image_dir)
    image = image.resize((45, 45), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(image)

    new_button = tk.Button(frame, height=height, width=width, bg=TOOL_BG, image=image)
    new_button.config(activebackground=TOOL_BG_CLICKED, command=command)
    new_button['borderwidth'] = 0.5
    new_button.image = image
    new_button.place(x=x, y=y, anchor="nw")
    new_button.bind("<Enter>", mouse_enter_tool)
    new_button.bind("<ButtonRelease>", mouse_release_tool)
    new_button.bind("<Leave>", mouse_leave_tool)
    return new_button


def make_img_button(frame, text, height, width, bg, fg, x, y, command, size, image_dir):
    image = tk.PhotoImage(file=image_dir)
    new_button = tk.Button(frame, text=text, height=height, width=width, bg=bg, fg=fg, image=image)
    new_button.config(activebackground=TOOL_BG_CLICKED, command=command)
    new_button.image = image
    new_button['font'] = font.Font(family='Helvetica', size=size)
    new_button['borderwidth'] = 0.5
    new_button.place(x=x, y=y, anchor="center")
    return new_button


def make_button(frame, text, height, width, bg, fg, x, y, command, size):
    new_button = tk.Button(frame, text=text, height=height, width=width, bg=bg, fg=fg)
    new_button.config(activebackground=TOOL_BG_CLICKED, command=command)
    new_button['font'] = font.Font(family='Helvetica', size=size)
    new_button['borderwidth'] = 1
    new_button.place(x=x, y=y, anchor="center")
    new_button.bind("<Enter>", mouse_enter_tile)
    new_button.bind("<Leave>", mouse_leave_tile)
    return new_button


def makeScale(frame, min_val, max_val, x, y, height, width, bg, fg, command):
    scale = tk.Scale(frame, orient='horizontal', from_=min_val, to=max_val, width=height, length=width, bg=bg, fg=fg)
    scale.config(highlightthickness=0, command=command)
    scale.place(x=x, y=y, anchor="center")
    return scale


def make_scaling_text_box(frame, bg, fg, height, width, font):
    text_box = tk.Text(frame, bg=bg, fg=fg, height=height, width=width, font=font)
    text_box.pack(side=tk.LEFT, fill=tk.BOTH, expand=tk.YES)
    return text_box


