import sys
import openpyxl

def main():
    if len(sys.argv) < 2:
        print("Please provide the name of the input file as a command-line argument")
        return
    
    if sys.version_info[0] < 3:
        input_func = raw_input
    else:
        input_func = input

    input_file = sys.argv[1]
    print("Input file is:", input_file)

    filename = sys.argv[1]
    wb = openpyxl.load_workbook(filename)
    ws = wb.active

    print("Waiting for input...")
    prompt = "Please enter the cell reference (e.g. A1): "
    cell_reference = input_func(prompt)
    cell_value = ws[cell_reference].value
    print(f"The value of cell {cell_reference} is: {cell_value}")

if __name__ == '__main__':
    main()
