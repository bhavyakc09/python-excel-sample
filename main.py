import openpyxl
import sys

def main():
    if len(sys.argv) > 1:
        cell_reference = sys.argv[1]
        print(f'Processing cell {cell_reference}')
    else:
        while True:
            try:
                print("Please enter the cell reference (e.g. A1): ")
                cell_reference = input()
                if not cell_reference:
                    raise ValueError('Cell reference cannot be empty')
                break
            except (EOFError, ValueError) as e:
                print(f'Error: {e}')

    wb = openpyxl.load_workbook('input_data.xlsx')
    ws = wb.active
    print(f'Value in cell {cell_reference}: {ws[cell_reference].value}')

if __name__ == '__main__':
    main()
