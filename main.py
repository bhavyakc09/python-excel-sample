import openpyxl

def main():
    while True:
        try:
            cell_reference = input('Please enter the cell reference (e.g. A1): ')
            if not cell_reference:
                raise ValueError('Cell reference cannot be empty')
            break
        except (EOFError, ValueError) as e:
            print(f'Error: {e}')
    print(f'Processing cell {cell_reference}')
