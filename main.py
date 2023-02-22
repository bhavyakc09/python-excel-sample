import openpyxl
import os

def main():
    wb = openpyxl.load_workbook('input_data.xlsx')
    ws = wb.active
    cell_reference = os.environ.get('CELL_REFERENCE')
    if not cell_reference:
        raise ValueError('CELL_REFERENCE environment variable is not set')
    print(f'Processing cell {cell_reference}')
    
    cell_value = ws[cell_reference].value
    print(f'Value in cell {cell_reference}: {cell_value}')

if __name__ == '__main__':
    main()
