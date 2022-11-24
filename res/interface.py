import tkinter as tk
def make_static_frame(frame, bg, w, h, x, y, anchor):
    new_frame = tk.Frame(frame, bg=bg)
    new_frame.place(width=w, height=h, x=x, y=y, anchor=anchor)
    return new_frame


def make_label(frame, text, bg, fg, x, y, anchor, size):
    label = tk.Label(frame, text=text, bg=bg, fg=fg)
    label.place(x=x, y=y, anchor=anchor)
    label['font'] = font.Font(family='Helvetica', size=size)
    return label




def mouse_enter_tool(e):
    if e.widget['background'] != TOOL_BG_CLICKED:
        e.widget['background'] = TOOL_BG_HOVER


def mouse_leave_tool(e):
    if e.widget['background'] != TOOL_BG_CLICKED:
        e.widget['background'] = TOOL_BG




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


