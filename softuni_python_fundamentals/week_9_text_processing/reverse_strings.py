while True:
    user_command = input()
    if user_command == "end":
        break
    text = user_command
    text_reversed = ""
    string_to_print = ""

    for chr in reversed(text):
        text_reversed += chr
    string_to_print = text+" = "+text_reversed
    print(string_to_print)
