from pathlib import Path
import csv
import json
import logic as lg
import interface as inf

def create_file(data_to_write, file_name = ''):
    if not file_name:
        event, values = inf.show_import_file_window("Exporting File")
        if all(values.values()):
            file_name = values['FILENAME']
    working_path = Path.cwd()
    path = working_path / "files_to_test" / file_name 
    if file_name:
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data_to_write) 

def open_file(file_name = '', input_list = [], input_dict = {}, input_summary_list = []):
    if not file_name:
        event, values = inf.show_import_file_window("Importing File")
        file_name = values['FILENAME']

    working_path = Path.cwd()
    try:
        if file_name:
            path = working_path / "files_to_test" / file_name 
            with open(path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                data_list = list(reader)
                if len(data_list) >= 4:
                    summary_list = data_list[len(data_list)-3:]
                    movements_list = data_list[:len(data_list)-4]
                else:
                    raise StopIteration
                categories_dict = {}
                for row in movements_list:
                    if categories_dict.get(row[3]):
                        categories_dict[row[3]].append(row)
                    else:
                        categories_dict[row[3]] = [row]
                return categories_dict, movements_list, summary_list
    except FileNotFoundError:
        inf.show_error_window("The specified file in working directory does not exist!")
    except StopIteration:
        inf.show_error_window("CSV file is empty")
    return input_dict, input_list, input_summary_list

def create_json (categories_dictionary):
    working_path = Path.cwd()
    file_path = working_path / "files_to_test" / lg.COLORS_CONFIG
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(categories_dictionary, json_file, indent=4)

def read_json_file(file_name = '', colors_categories_dict = {}):
    working_path = Path.cwd()
    file_path = working_path / "files_to_test" / file_name

    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            colors_categories_dict = json.load(json_file)
    except FileNotFoundError:
        inf.show_error_window("The config .json file is not in working directory")
    except json.JSONDecodeError:
        inf.show_error_window("Could not decode .json file located in working path")
    return colors_categories_dict
