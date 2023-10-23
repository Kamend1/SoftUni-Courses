class Party:
    def __init__(self):
        self.people = []

party = Party()
name_input = input()

while name_input != "End":
    party.people.append(name_input)
    name_input = input()

print(f"Going: {', '.join(party.people)}")
print(f"Total: {len(party.people)}")
