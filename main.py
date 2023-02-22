import openpyxl
import sys

def main():
    wb = openpyxl.load_workbook('input_data.xlsx')
    ws = wb.active
    cell_reference = sys.argv[1]
    print(f'Processing cell {cell_reference}')
    
    while True:
        try:
            sys.stdout.flush()
            print("Please enter the cell reference (e.g. A1): ")
            cell_reference = raw_input()  # use raw_input instead of input
            if not cell_reference:
                raise ValueError('Cell reference cannot be empty')
            break
        except (EOFError, ValueError) as e:
            print(f'Error: {e}')

if __name__ == '__main__':
    main()
