import openpyxl
import sys

def get_input(prompt):
    try:
        return raw_input(prompt)
    except NameError:
        return input(prompt)
    
    print(get_input("Please enter the cell reference (e.g. A1): "))
    
def main(input_func=input):
    
    # Read the command-line arguments
    input_file = sys.argv[1]
    cell_reference = sys.argv[2]

    # Load the input workbook
    workbook = openpyxl.load_workbook(input_file, data_only=True)

    # Get the value of the specified cell
    worksheet = workbook.active
    cell = worksheet[cell_reference]
    cell_value = cell.value

    # Print the cell value
    print(f"The value of cell {cell_reference} is {cell_value}")

    # Prompt the user for input
    cell_reference = input_func("Please enter the cell reference (e.g. A1): ")

    # Get the value of the new cell reference
    cell = worksheet[cell_reference]
    cell_value = cell.value

    # Print the cell value
    print(f"The value of cell {cell_reference} is {cell_value}")

if __name__ == '__main__':
    main()
