with open('output_data.txt', 'r') as f:
    output_data = f.read()

# replace with your expected output data
expected_output_data = '[[2, 4], [6, 8]]'

assert output_data == expected_output_data, 'Output data does not match expected data!'
