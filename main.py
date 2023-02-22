import openpyxl
import os

def main():
    wb = openpyxl.load_workbook('input_data.xlsx')
    ws = wb.active
    cell_reference = os.environ.get('CELL_REFERENCE')
    print(f'Processing cell {cell_reference}')

    while True:
        try:
            sys.stdout.flush()
            print("Please enter the cell reference (e.g. A1): ")
            cell_reference = input()
            if not cell_reference:
                raise ValueError('Cell reference cannot be empty')
            break
        except (EOFError, ValueError) as e:
            print(f'Error: {e}')
