import openpyxl
import sys

def get_input(prompt):
    try:
        return input(prompt)
    except (NameError, EOFError):
        return raw_input(prompt) if 'raw_input' in globals() else input(prompt)

def main():
    # Read the command-line arguments
    input_file = sys.argv[1]

    # Load the input workbook
    workbook = openpyxl.load_workbook(input_file, data_only=True)

    # Get the sheet name from the user
    sheet_name = get_input("Please enter the name of the sheet: ")

    # Get the cell reference from the user
    cell_reference = get_input("Please enter the cell reference (e.g. A1): ")

    # Get the value of the specified cell
    worksheet = workbook[sheet_name]
    cell = worksheet[cell_reference]
    cell_value = cell.value

    # Print the cell value
    print(f"The value of cell {cell_reference} is {cell_value}")
