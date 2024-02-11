from tkinter import Tk, Canvas


def window_setup():
    root = Tk()

    root.title("GUI Shop")
    root.geometry("700x600")
    root.resizable(False, False)
    root.configure(bg="light blue")

    return root


def define_frame():
    frame = Canvas(root, width=700, height=700)
    frame.grid(row=0, column=0)

    return frame


root = window_setup()
frame = define_frame()
