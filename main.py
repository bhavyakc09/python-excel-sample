import sys
import openpyxl

if len(sys.argv) > 1:
    cell_reference = sys.argv[1]
else:
    cell_reference = input('Please enter the cell reference (e.g. A1): ')

workbook = openpyxl.load_workbook('input_data.xlsx')
worksheet = workbook.active
cell = worksheet[cell_reference]
print(cell.value)

