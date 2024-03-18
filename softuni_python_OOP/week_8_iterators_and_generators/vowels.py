class vowels:
    VOWELS = ['a', 'o', 'e', 'i', 'u', 'y']

    def __init__(self, text: str):
        self.text = text
        self.index = 0
        self.vowels_list = [c for c in self.text if c.lower() in self.VOWELS]

    def __iter__(self):
        return self.text
        # return iter(self.vowels_list)

    def __next__(self):
        if self.index < len(self.vowels_list):
            idx = self.index
            self.index += 1
            return self.vowels_list[idx]
        raise StopIteration

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

