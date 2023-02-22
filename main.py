import sys
import openpyxl

def main():
    # parse command line arguments
    if len(sys.argv) < 2:
        print('Please provide a cell reference (e.g. A1) as a command line argument')
        return
    cell_reference = sys.argv[1]

    workbook = openpyxl.load_workbook('input_data.xlsx')
    worksheet = workbook.active
    print("Before input prompt")
    cell_reference = input('Please enter the cell reference (e.g. A1): ') or 'A1'
    print("After input prompt")
    cell = worksheet[cell_reference]
    print(cell.value)

if __name__ == "__main__":
    main()
