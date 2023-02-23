import sys
import openpyxl

def main():
    if len(sys.argv) < 2:
        print("Please provide the name of the input file as a command-line argument")
        return
    
    filename = sys.argv[1]
    wb = openpyxl.load_workbook(filename)
    ws = wb.active
    cell_reference = ws['A1'].value
    
    # Rest of your code here

if __name__ == '__main__':
    main()
