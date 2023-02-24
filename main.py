import sys
import openpyxl

def main():
    print(sys.argv) # check that the command-line arguments are being passed correctly
    
    if len(sys.argv) < 3:
        print("Please provide the name of the input file and the cell reference as command-line arguments")
        return
    
    input_file = sys.argv[1]
    print("Input file is:", input_file)

    filename = sys.argv[1]
    wb = openpyxl.load_workbook(filename)
    ws = wb.active

    print("Waiting for input...")
    cell_reference = sys.argv[2]
    cell_value = ws[cell_reference].value
    cell_reference = input("Please enter the cell reference (e.g. A1): ")

    print(f"The value of cell {cell_reference} is: {cell_value}")

if __name__ == "__main__":
    main()
