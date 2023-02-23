import time

def main():
    print("Main function called")
    input_file = sys.argv[1]

    if len(sys.argv) < 2:
        print("Please provide the name of the input file as a command-line argument")
        return
    
    print("Input file is:", input_file)

    filename = sys.argv[1]
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    time.sleep(1) # wait for 1 second
    cell_reference = input("Please enter the cell reference (e.g. A1): ")
