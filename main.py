import openpyxl
import sys

def main():
    wb = openpyxl.load_workbook('input_data.xlsx')
    ws = wb.active
    cell_reference = sys.argv[1]
    print(f'Processing cell {cell_reference}')

if __name__ == '__main__':
    main()


