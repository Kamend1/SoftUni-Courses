from tkmacosx import Button
from tkinter import Entry
from canvas import root, frame
from helpers import clean_screen



def starting_screen():
    register_button = Button(
        root,
        text="Register",
        bg="green",  # background color
        fg="white",  # font color
        bd=0,  # border = 0
        width=90,
        height=40,
        command=register_screen
    )

    login_button = Button(
        root,
        text="Login",
        bg="blue",
        fg="white",
        bd=0,
        width=90,
        height=40,
        command=login_screen
    )

    frame.create_window(350, 260, window=register_button)
    frame.create_window(350, 310, window=login_button)


def register_screen():
    clean_screen()

    frame.create_text(100, 50, text="First Name:")
    frame.create_text(100, 100, text="Last Name:")
    frame.create_text(100, 150, text="Username:")
    frame.create_text(100, 200, text="Password:")

    frame.create_window(230, 50, window=first_name_box)
    frame.create_window(230, 100, window=last_name_box)
    frame.create_window(230, 150, window=username_box)
    frame.create_window(230, 200, window=password_box)

    register_button = Button(
        root,
        text="Register",
        bg="green",
        fg="white",
        bd=0,
        width=90,
        height=40,
        command=registration_of_user
    )

    frame.create_window(315, 250, window=register_button)


def login_screen():
    clean_screen()

    frame.create_text(100, 50, text="Username:")
    frame.create_text(100, 100, text="Password:")

    frame.create_window(230, 50, window=username_box)
    frame.create_window(230, 100, window=password_box)

    frame.create_window(300, 150, window=login_button)


def registration_of_user():
    user_data_dict = {
        'First name': first_name_box.get(),
        'Last name': last_name_box.get(),
        'Username': username_box.get(),
        'Password': password_box.get(),
    }

    if verify_registration_data(user_data_dict):
        pass



def verify_registration_data(user_data_dict):
    frame.delete("error")

    for k, v in user_data_dict.items():
        if not v.strip():
            frame.create_text(
                200,
                300,
                text=f"{k} cannot be empty!",
                fill="red",
                tags="error",
            )

            return False

def logging_user_in_shop():
    pass


first_name_box = Entry(root, bd=0)
last_name_box = Entry(root, bd=0)
username_box = Entry(root, bd=0)
password_box = Entry(root, bd=0, show="*")

login_button = Button(
    root,
    text="Login",
    bg="blue",
    fg="white",
    bd=0,
    command=logging_user_in_shop,
)

login_button["state"] = "disabled"
