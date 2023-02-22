import openpyxl

def main():
    wb = load_workbook('input_data.xlsx')
    ws = wb.active
    
     if len(sys.argv) > 1:
        cell_reference = sys.argv[1]
    else:
        cell_reference = 'A1'
        
    while True:
        try:
            cell_reference = input('Please enter the cell reference (e.g. A1): ')
            if not cell_reference:
                raise ValueError('Cell reference cannot be empty')
            break
        except (EOFError, ValueError) as e:
            print(f'Error: {e}')
    print(f'Processing cell {cell_reference}')

   
