import sys

def get_input(prompt):
    try:
        return input(prompt)
    except NameError:
        return raw_input(prompt)

cell_reference = get_input("Please enter the cell reference (e.g. A1): ")
print(cell_reference)
