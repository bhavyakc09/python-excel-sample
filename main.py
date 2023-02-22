import openpyxl

workbook = openpyxl.load_workbook('input_data.xlsx')
worksheet = workbook.active

cell_reference = input("Please enter the cell reference (e.g. A1): ")
cell = worksheet[cell_reference]
print(cell.value)
