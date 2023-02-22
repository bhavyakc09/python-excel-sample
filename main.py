import os
import openpyxl

# Get the current working directory
cwd = os.getcwd()

# Define the path to the input file relative to the current working directory
input_file_path = os.path.join(cwd, 'input_data.xlsx')

# Load the workbook
workbook = openpyxl.load_workbook(input_file_path)

# Select the first sheet
sheet = workbook.active

# Prompt the user to enter the cell reference
cell_reference = input("Enter the cell reference (e.g. A1): ")

# Read the value from the corresponding cell
value = sheet[cell_reference].value

# Print the input value
print(f"{cell_reference}: {value}")
