from tkmacosx import Button
from tkinter import Entry
from canvas import root, frame
from helpers import clean_screen, get_password_hash
from softuni_python_advanced.week_9_modules.gui_shop.buying_page import display_products
from json import dump, loads


def get_users_data():
    info_data = []  # [{}, {}, ...]

    with open("db/users_information.txt", "r") as users_file:
        for line in users_file:
            info_data.append(loads(line))

    return info_data


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
        with open("db/users_information.txt", "a") as users_file:
            user_data_dict["Password"] = get_password_hash(user_data_dict["Password"])
            dump(user_data_dict, users_file)
            users_file.write("\n")
            display_products()



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

    users_data = get_users_data()

    for user in users_data:
        if user["Username"] == user_data_dict["Username"]:
            frame.create_text(
                200,
                300,
                text="Username is already taken!",
                fill="red",
                tags="error",
            )

            return False

    return True

def logging():
    if check_login():
        display_products()
    else:
        frame.create_text(
            200,
            200,
            text="Invalid username or password!",
            fill="red",
            tags="error",
        )


def check_login():
    users_data = get_users_data()

    user_username = username_box.get()
    user_password = get_password_hash(password_box.get())

    for user in users_data:
        current_user_username = user["Username"]
        current_user_password = user["Password"]

        if current_user_username == user_username and current_user_password == user_password:
            return True

    return False


def change_login_button_status(event):
    info = [
        username_box.get(),
        password_box.get(),
    ]

    for el in info:
        if not el.strip():
            login_button["state"] = "disabled"
            break
    else:
        login_button["state"] = "normal"


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
    command=logging,
)

login_button["state"] = "disabled"

root.bind("<KeyRelease>", change_login_button_status)