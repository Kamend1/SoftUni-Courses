class take_skip:

    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.number = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count > 0:
            current = self.number
            self.number += self.step
            self.count -= 1
            return current
        raise StopIteration


numbers = take_skip(2, 6)
for number in numbers:
    print(number)



