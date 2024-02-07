from softuni_python_advanced.week_9_modules.fibonacci_sequence.calc_fib import create_sequence, locate

fib_sequence = []

while True:
    command = input().split()

    if command[0] == 'Stop':
        break

    if command[0] == "Create":
        fib_sequence = create_sequence(int(command[2]))
        print(*fib_sequence)
    elif command[0] == "Locate":
        locate(int(command[1]), fib_sequence)
