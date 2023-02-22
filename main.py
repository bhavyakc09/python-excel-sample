import sys
from openpyxl import load_workbook

def main(cell_reference='A1'):
    wb = load_workbook('input_data.xlsx')
    ws = wb.active
    print(f'Processing cell {cell_reference}')
    # do something with the worksheet and cell reference here

if __name__ == '__main__':
    cell_reference = sys.argv[1] if len(sys.argv) > 1 else 'A1'
    main(cell_reference)

