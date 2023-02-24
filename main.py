import sys
import openpyxl

def main():
    if len(sys.argv) < 3:
        print("Please provide the name of the input file and the cell reference as command-line arguments")
        return
    
    input_file = sys.argv[1]
    cell_reference = sys.argv[2]
    
    print("Input file is:", input_file)
    print("Cell reference is:", cell_reference)

    wb = openpyxl.load_workbook(input_file)
    ws = wb.active

    cell_value = ws[cell_reference].value
    print(f"The value of cell {cell_reference} is: {cell_value}")
