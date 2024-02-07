def create_sequence(num):
    seq = [0, 1]
    for _ in range(num - 2):
        next_number = seq[-1] + seq[-2]
        seq.append(next_number)
    return seq


def locate(num, sequence):
    if num in sequence:
        index = sequence.index(num)
        print(f"The number - {num} is at index {index}")
    else:
        print(f"The number {num} is not in the sequence")
