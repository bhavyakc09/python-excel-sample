import sys
import openpyxl

def main():
    if len(sys.argv) < 3:
        print("Please provide the name of the input file and cell reference as command-line arguments")
        return
    
    input_file = sys.argv[1]
    print("Input file is:", input_file)

    filename = sys.argv[1]
    wb = openpyxl.load_workbook(filename)
    ws = wb.active

    cell_reference = sys.argv[2]
    cell_value = ws[cell_reference].value
    print(f"The value of cell {cell_reference} is: {cell_value}")
