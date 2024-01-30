import re
import tkinter as tk
from tkinter import messagebox


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


def validate_email():
    try:
        current_email_address = email_address.get()
        if current_email_address == 'End':
            return

        matches_at_symbol = re.findall(pattern_at_symbol, current_email_address, flags=re.IGNORECASE)
        matches = re.findall(pattern, current_email_address, flags=re.IGNORECASE)

        if not matches_at_symbol:
            raise MustContainAtSymbolError("Email must contain @")

        name = matches[0][1]
        domain = matches[0][4]
        print(name, domain)

        if len(name) < MIN_NAME_CHARS_COUNT:
            raise NameTooShortError("Name must be more than 4 characters")

        if domain not in VALID_DOMAINS:
            raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

        output = "Email is valid"

    except (MustContainAtSymbolError, NameTooShortError, InvalidDomainError) as e:
        output = str(e)

    return output

def update_label_text():
    result = validate_email()
    if result != "Email is valid":
        error_message_label.config(text=result, foreground='red', font='Bold')
    else:
        error_message_label.config(text=result, foreground='green', font='Bold')


def exit_application():
    confirmation = messagebox.askyesno("Confirmation","Are you sure you want to exit")
    if confirmation:
        root.destroy()


pattern = r"(\b([A-Za-z0-9][A-Za-z0-9\.\-\_]+)(@)([A-Za-z]+[\-]?[A-Za-z]+)(\.[\.a-z]+)*\b)"
pattern_at_symbol = r"@"
VALID_DOMAINS = ('.com', '.bg', '.org', '.net')
MIN_NAME_CHARS_COUNT = 4
output = ''

root = tk.Tk()
root.title("Email Validator")
root.geometry("900x500")

email_address = tk.Entry(root)
email_address.place(x=50, y=60, width=400, height=30)

email_label = tk.Label(root, text="Enter a valid email address")
email_label.place(x=50, y=30, width=400)

validate_button = tk.Button(root, text="Validate", command=update_label_text)
validate_button.place(x=460, y=60, width=200, height=30)

result = validate_email()
error_message_label = tk.Label(root, text="")
error_message_label.place(x=50, y=100, width=400, height=30)

exit_button = tk.Button(root, text="Exit", command=exit_application)
exit_button.place(x=400, y=400, width=100, height=30)

root.mainloop()
