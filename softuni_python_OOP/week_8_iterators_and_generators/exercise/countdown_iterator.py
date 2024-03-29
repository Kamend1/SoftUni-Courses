class countdown_iterator:

    def __init__(self, number: int):
        self.number = number

    def __iter__(self):
        return self

    def __next__(self):
        if self.number >= 0:
            current = self.number
            self.number -= 1
            return current
        raise StopIteration


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
