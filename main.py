import openpyxl
import ipywidgets as widgets
from IPython.display import display

def main():
    # load workbook and active worksheet
    workbook = openpyxl.load_workbook('input_data.xlsx')
    worksheet = workbook.active

    # create Text widget for input
    cell_reference = widgets.Text(value='A1', description='Cell reference:')

    # display the Text widget
    display(cell_reference)

    # wait for user to submit input
    button = widgets.Button(description='Submit')
    display(button)
    out = widgets.Output()

    def on_button_click(_):
        # get cell value
        cell = worksheet[cell_reference.value]
        print(cell.value)

    button.on_click(on_button_click)

if __name__ == '__main__':
    main()
