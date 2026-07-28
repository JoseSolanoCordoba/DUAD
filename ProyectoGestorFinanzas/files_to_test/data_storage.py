import os
import csv
import json
import interface as inf

def create_file(data_to_write, file_name = ''):
    if not file_name:
        event, values = inf.show_import_file_window()
        if all(values.values()):
            file_name = values['FILENAME']
    working_path = os.getcwd()
    path = working_path + "\\" + "files_to_test" + "\\" + file_name + ".csv"
    if file_name:
        with open(path, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerows(data_to_write) 

def open_file(file_name = '', input_list = [], input_dict = {}, input_totals_list = []):
    if not file_name:
        event, values = inf.show_import_file_window()
        file_name = values['FILENAME']

    working_path = os.getcwd()
    try:
        if file_name:
            path = working_path + "\\" + "files_to_test" + "\\" + file_name + ".csv"
            with open(path, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader)
                data_list = list(reader)
                totals_list = data_list[len(data_list)-3:]
                data_list = data_list[:len(data_list)-4]
                data_dict = {}
                for row in data_list:
                    if data_dict.get(row[0]):
                        data_dict[row[0]].append(row)
                    else:
                        data_dict[row[0]] = [row]
                return data_list, data_dict, totals_list
    except FileNotFoundError:
        inf.show_error_window("The specified file in working directory does not exist!")
    except StopIteration:
        inf.show_error_window("CSV file is empty")
    return input_list, input_dict, input_totals_list

def create_json (data_dictionary):
    working_path = os.getcwd()
    file_path = working_path + "\\" + "files_to_test" + "\\" + "Colors_Config.json"
    with open(file_path, 'w', encoding='utf-8') as json_file:
        json.dump(data_dictionary, json_file, indent=4)

def read_json_file(file = '', colors_data_dict = {}):
    working_path = os.getcwd()
    file_path = working_path + "\\" + "files_to_test" + "\\" + file + ".json"

    try:
        with open(file_path, 'r', encoding='utf-8') as json_file:
            colors_data_dict = json.load(json_file)
    except FileNotFoundError:
        inf.show_error_window("The config .json file is not in working directory")
    except json.JSONDecodeError:
        inf.show_error_window("Could not decode .json file located in working path")
    return colors_data_dict
