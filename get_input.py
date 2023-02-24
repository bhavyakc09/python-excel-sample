import sys

def get_input(prompt):
    try:
        return raw_input(prompt)
    except NameError:
        return input(prompt)

cell_reference = get_input("Please enter the cell reference (e.g. A1): ")
print(cell_reference)
