import sys
import openpyxl

def main():
    # parse command line arguments
    if len(sys.argv) < 2:
        cell_reference = input("Please enter the cell reference (e.g. A1): ")
    else:
        cell_reference = sys.argv[1]

    # load the workbook and select the active worksheet
    workbook = openpyxl.load_workbook('input_data.xlsx')
    worksheet = workbook.active

    # retrieve the cell value and print it
    cell = worksheet[cell_reference]
    print(cell.value)

if __name__ == '__main__':
    main()
