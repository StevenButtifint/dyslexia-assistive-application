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


