number_available_electrons = int(input())
filled_atom_shells = []

position = 1

while number_available_electrons > 0:
    atom_shell_electrons = 2 * (position ** 2)
    if atom_shell_electrons > number_available_electrons:
        if number_available_electrons > 0:
            atom_shell_electrons = number_available_electrons
    filled_atom_shells.append(atom_shell_electrons)
    number_available_electrons -= atom_shell_electrons
    position += 1

print(filled_atom_shells)
