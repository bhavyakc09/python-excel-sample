import sys
import os
os.environ['CELL_REFERENCE'] = 'A1'

def main():
    cell_reference = input("Please enter the cell reference (e.g. A1): ")
    cell_value = ws[cell_reference].value
    print(f"Value in cell {cell_reference}: {cell_value}")

if __name__ == '__main__':
    main()
