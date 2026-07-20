import PySimpleGUI as sg
import logic as lg
import data_storage as dst

def add_category_name_window():
    add_title_layout = [[sg.Text("Enter the new title to add:")],
                    [sg.Input(key = 'TITLEINPUT')],
                    [sg.Input(visible = False, key = 'COLOR'), sg.ColorChooserButton("Choose Category Color"), sg.Text("(Optional)")],
                    [sg.Button('Ok')]]
    add_title_window = sg.Window('Adding New Title', add_title_layout)
    event, values = add_title_window.read()
    add_title_window.close()
    return event, values

def add_movement_window(window_title):
    add_income_outcome_layout = [[sg.Text("Enter the title:")],
                    [sg.Input(size = (15), key = 'TITLE')],
                    [sg.Text("Enter the amount:")],
                    [sg.Input(size = (15), key = 'AMOUNT')],
                    [sg.Text("Enter Date:")],
                    [sg.Input("yyyy/mm/dd", size = (10), key = 'DATE')],
                    [sg.Button('Ok')]]
    add_movement_window = sg.Window(window_title, add_income_outcome_layout)
    event, values = add_movement_window.read()
    add_movement_window.close()
    return event, values

def show_import_file_window():
    import_file_layout = [[sg.Text("Enter the file name:")],
                    [sg.Input(key = 'FILENAME')],
                    [sg.Button('Ok')]]
    import_file_window = sg.Window('Opening File', import_file_layout)
    event, values = import_file_window.read()
    import_file_window.close()
    return event, values

def show_error_window(error_message):
    error_layout = [[sg.Text(error_message, font = ("Helvetica", 20), text_color = 'red')],]
    error_window = sg.Window("ERROR", error_layout)
    error_window.read()
    error_window.close()
    
def show_main_window(financial_object):
    main_layout = [[sg.Text("Date Filter:"),
                    sg.Input("From: yyyy/mm/dd", size = (16), key = 'DATE1'),
                    sg.Input("To: yyyy/mm/dd", size = (14), key = 'DATE2'),
                    sg.Button('Filter'), sg.Button('Clear Filter')], 
                    [sg.Table(values = financial_object.data_list, headings = financial_object.header,
                    row_colors = financial_object.colors_list, 
                    auto_size_columns = False, col_widths=(20, 10, 10, 10),  justification='left',
                    key = 'TABLE')],
                    [sg.Button('Add New Title'), sg.Button('Add Income'),
                    sg.Button('Add Outcome'), sg.Button('Export File'), sg.Button('Import File')],
                    [sg.Button('Ok'), sg.Button('Quit')],]
    
    main_window = sg.Window('Financial Manager', main_layout)

    while True:
        event, values = main_window.read()

        if event == sg.WINDOW_CLOSED or event == 'Quit':
            dst.create_file(financial_object.data_list, "Financial_Status")
            break
        elif event and values:
            data_to_show, colors_to_show = financial_object.actions_management(event, values)
            main_window['TABLE'].update(values = data_to_show,  row_colors = colors_to_show)
    main_window.close()

