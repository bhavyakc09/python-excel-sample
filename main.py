import sys
import os
os.environ['CELL_REFERENCE'] = 'A1'

def main():
    # Get the cell reference from the environment variable
    cell_reference = os.environ.get('CELL_REFERENCE')

    if cell_reference is None:
        raise ValueError('CELL_REFERENCE environment variable is not set')

    # Load the workbook
    wb = load_workbook(filename='example.xlsx')

    # Get the active worksheet
    ws = wb.active

    # Get the value in the cell
    cell_value = ws[cell_reference].value

    # Print the cell value
    print(f'Value in cell {cell_reference}: {cell_value}')
