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


