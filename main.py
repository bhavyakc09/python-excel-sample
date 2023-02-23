import sys
import openpyxl

def main():
    print("Main function called")
    if len(sys.argv) < 2:
        print("Please provide the name of the input file as a command-line argument")
        return
    
    input_file = sys.argv[1]
    wb = openpyxl.load_workbook(input_file)
    ws = wb.active
    cell_reference = input("Please enter the cell reference (e.g. A1): ")
    cell_value = ws[cell_reference].value
    print(f"The value of cell {cell_reference} is {cell_value}")


if __name__ == '__main__':
    main()
