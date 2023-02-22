import sys
import openpyxl

def main():
    # parse command line arguments
    if len(sys.argv) < 2:
        print("Please provide a cell reference (e.g. A1) as a command line argument.")
        return
    cell_reference = sys.argv[1]

workbook = openpyxl.load_workbook('input_data.xlsx')
worksheet = workbook.active
cell_reference = raw_input("Please enter the cell reference (e.g. A1): ")
print(cell.value)

