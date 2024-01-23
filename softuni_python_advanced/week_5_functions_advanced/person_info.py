def get_info(name, age, town):
    result = f"This is {name} from {town} and he is {age} years old"
    return result

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))

