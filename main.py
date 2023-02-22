import argparse
import openpyxl

parser = argparse.ArgumentParser(description='Get value from cell in Excel file.')
parser.add_argument('cell_reference', help='The cell reference (e.g. A1)')
args = parser.parse_args()

input_file_path = 'input_data.xlsx'

workbook = openpyxl.load_workbook('input_data.xlsx')
worksheet = workbook.active

cell = worksheet[args.cell_reference]
print(cell.value)

