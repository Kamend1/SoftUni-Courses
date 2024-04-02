from copy import deepcopy


class HashTable:

    def __init__(self):
        self.__keys = [None, None, None, None]
        self.__values = [None, None, None, None]
        self.__length = 4

    def __len__(self):
        return self.__length

    def __setitem__(self, key, value):
        try:
            existing_value_index = self.__keys.index(key)
            self.__values[existing_value_index] = value
        except ValueError:
            if self.count == self.__length:
                self.__resize()
            index = self.__find_index(self.hash(key))
            self.__keys[index] = key
            self.__values[index] = value

    @property
    def count(self):
        return len([el for el in self.__keys if el is not None])

    def __getitem__(self, item):
        try:
            index = self.__keys.index(item)
            return self.__values[index]
        except ValueError:
            raise KeyError("Key does not exist!")

    def __find_index(self, index):
        if index == self.__length:
            index = 0
        if self.__keys[index] is None:
            return index
        return self.__find_index(index + 1)

    def __resize(self):
        self.__keys = self.__keys + [None] * self.__length
        self.__values = self.__values + [None] * self.__length
        self.__length *= 2

    def hash(self, key: str):
        return sum([ord(el) for el in key]) % self.__length

    def add(self, key: str, value: any):
        self.__setitem__(key, value)

    def get(self, key: str, return_default_value=None):
        try:
            index = self.__keys.index(key)
            return self.__values[index]
        except ValueError:
            return return_default_value

    def sort(self):
        copy_keys = [el for el in self.__keys if el is not None]
        copy_values = [el for el in self.__values if el is not None]

        result = list(zip(copy_keys, copy_values))
        sorted_result = sorted(result, key=lambda x: x[0])
        table = HashTable()
        table._Hashtable__keys = [t[0] for t in sorted_result]
        table._Hashtable__values = [t[1] for t in sorted_result]
        table._Hashtable__length = self.__length
        diff = self.__length - table.count
        table._Hashtable__keys += [None] * diff
        table._Hashtable__values += [None] * diff
        return table


    def __str__(self):
        result = [f"{self.__keys[index]}: {self.__values[index]}" for index in range(self.__length) if self.__keys[index] is not None]
        return "{" + ', '.join(result) + "}"


table = HashTable()

table["name"] = "Peter"
table["age"] = 25

print(table)
print(table.get("name"))
print(table["age"])
print(len(table))
