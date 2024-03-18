from math import ceil


class sequence_repeat:

    def __init__(self, sequence, count):
        self.sequence = sequence
        self.count = count
        self.index = -1
        self.repeated_sequence = sequence * ceil(self.count / len(self.sequence) )

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            self.index += 1
            self.count -= 1
            return self.repeated_sequence[self.index]
        raise StopIteration

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
