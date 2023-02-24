import openpyxl
import sys

def main():
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

if __name__ == '__main__':
    main()
