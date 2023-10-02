def data_types(data_type, user_data):
    if data_type == 'int':
        result = int(user_data) * 2
    elif data_type == 'real':
        result = f"{float(user_data) * 1.5:.2f}"
    elif data_type =='string':
        result = "$" + str(user_data) + "$"
    return result

data_type = input()
user_data = input()

print(data_types(data_type, user_data))
