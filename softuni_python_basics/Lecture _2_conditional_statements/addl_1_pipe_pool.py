volume_pool = int(input())
debit_pipe1 = int(input())
debit_pipe2 = int(input())
time_worker_absent = float(input())

water_input = time_worker_absent * (debit_pipe2 + debit_pipe1)
percent_full = (water_input / volume_pool) * 100
percent_pipe1 = ((time_worker_absent * debit_pipe1) / water_input) * 100
percent_pipe2 = ((time_worker_absent * debit_pipe2) / water_input) * 100

if percent_full <= 100:
    print(f"The pool is {percent_full:.2f}% full. \
    Pipe 1: {percent_pipe1:.2f}%. \
    Pipe 2: {percent_pipe2:.2f}%.")
else:
    water_overflow = water_input - volume_pool
    print(f"For {time_worker_absent} hours the pool overflows with {water_overflow} liters.")

