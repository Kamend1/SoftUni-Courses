from collections import deque
def stock_availability(user_list, command, *args):
    user_list = deque(user_list)

    if command == 'delivery':
        for arg in args:
            user_list.append(arg)
    elif command == 'sell':
        if not args:
            user_list.popleft()
        elif type(args[0]) == int:
            for _ in range(int(args[0])):
                user_list.popleft()
        else:
            for arg in args:
                if arg in user_list:
                    user_list = [x for x in user_list if x != arg]

    result_list = []
    for el in user_list:
        result_list.append(el)

    return result_list


print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))
