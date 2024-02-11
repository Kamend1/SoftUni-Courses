from collections import deque

pizza_orders = deque(int(x) for x in input().split(', '))
employee_capacity = [int(x) for x in input().split(', ')]
total_pizzas_made = 0

while True:
    if pizza_orders:
        current_order = pizza_orders.popleft()
        if current_order <= 0 or current_order > 10:
            continue
    else:
        break

    if employee_capacity:
        current_capacity = employee_capacity.pop()
    else:
        pizza_orders.appendleft(current_order)
        break

    if current_order <= current_capacity:
        total_pizzas_made += current_order
    else:
        total_pizzas_made += current_capacity
        pizza_orders.appendleft(current_order - current_capacity)



if not pizza_orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas_made}")
    if employee_capacity:
        print(f"Employees: {', '.join(str(x) for x in employee_capacity)}")
else:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join(str(x) for x in pizza_orders)}")
