import openpyxl

def main():
    # Load the workbook
    workbook = openpyxl.load_workbook('input_data.xlsx')

    # Get the active worksheet
    worksheet = workbook.active

    # Get the cell reference from the user
    cell_reference = input('Please enter the cell reference (e.g. A1): ')

    # Get the cell value
    cell_value = worksheet[cell_reference].value

    # Print the cell value
    print(f'The value of cell {cell_reference} is {cell_value}')

if __name__ == '__main__':
    main()
