import sys
import openpyxl

# Define the path to the input file
input_file_path = 'input_data.xlsx'

# Load the workbook
workbook = openpyxl.load_workbook(input_file_path)

# Select the first sheet
sheet = workbook.active

# Get the cell reference from the command line argument
cell_reference = sys.argv[1]

# Read the value from the corresponding cell
value = sheet[cell_reference].value

# Print the input value
print(f"{cell_reference}: {value}")

