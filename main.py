import openpyxl
import sys

def main():
    wb = openpyxl.load_workbook('input_data.xlsx')
    ws = wb.active
    while True:
        try:
            sys.stdout.flush()
            cell_reference = input('Please enter the cell reference (e.g. A1): ')
            if not cell_reference:
                raise ValueError('Cell reference cannot be empty')
            break
        except (EOFError, ValueError) as e:
            print(f'Error: {e}')
    print(f'Processing cell {cell_reference}')

if __name__ == '__main__':
    main()


