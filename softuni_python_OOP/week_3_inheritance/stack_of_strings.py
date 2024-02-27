class Stack:

    def __init__(self):
        self.data = []

    def push(self, element: str):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return False if self.data else True

        # if len(self.data) == 0:
        #     is_empty = True
        # else:
        #     is_empty = False
        #
        # return is_empty

    def __str__(self):
        result = ', '.join(reversed(self.data))
        return f"[{result}]"
