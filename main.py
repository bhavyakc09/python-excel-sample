import sys
import openpyxl

def main():
    if len(sys.argv) < 2:
        print("Please provide the name of the input file as a command-line argument")
        return
    
    filename = sys.argv[1]
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    
    # Prompt the user to enter a cell reference
    cell_reference = input("Please enter the cell reference (e.g. A1): ")
    cell_value = ws[cell_reference].value
    
    print(f"The value of cell {cell_reference} is: {cell_value}")


if __name__ == '__main__':
    main()

