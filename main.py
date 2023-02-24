import sys
import openpyxl

def main():
    if len(sys.argv) < 2:
        print("Please provide the name of the input file as a command-line argument")
        return
    
    input_file = sys.argv[1]
    print("Input file is:", input_file)

    filename = sys.argv[1]
    wb = openpyxl.load_workbook(filename)
    ws = wb.active

    with open('cell_reference.txt', 'r') as f:
        cell_reference = f.read().strip()
    cell_value = ws[cell_reference].value
    print(f"The value of cell {cell_reference} is: {cell_value}")
