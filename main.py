import openpyxl

# Define the path to the input file
input_file_path = 'input_data.xlsx'

# Load the workbook
workbook = openpyxl.load_workbook('input_data.xlsx')

# Select the first sheet
sheet = workbook.active

# Prompt the user to enter the cell reference
cell_reference = input("Please enter the cell reference: A1 ")

# Read the value from the corresponding cell
value = sheet[cell_reference].value

# Print the input value
print(f"{cell_reference}: {value}")
