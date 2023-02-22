import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <cell_reference>")
        return
    cell_reference = sys.argv[1]
    if not cell_reference:
        raise ValueError('CELL_REFERENCE environment variable is not set')
    print(f'Processing cell {cell_reference}')
    
    cell_value = ws[cell_reference].value
    print(f'Value in cell {cell_reference}: {cell_value}')

if __name__ == '__main__':
    main()
