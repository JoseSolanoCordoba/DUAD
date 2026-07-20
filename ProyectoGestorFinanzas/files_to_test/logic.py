from datetime import datetime, date
import itertools
import interface as inf
import data_storage as dst


class Category:
    def __init__(self):
        super().__init__()
        self.category_name = ""

    @property
    def capitalized_category(self):
        self.category_name = self.category_name.capitalize()
        return self.category_name
    
    def build_category(self):
        category_string = self.capitalized_category
        category_entry = [category_string,"","",""]
        return category_entry

    def add_category_entry(self):
        event, values = inf.add_category_name_window()
        self.category_name = values['TITLEINPUT']
        if self.category_name:
            category_color = values['COLOR']
            if not category_color:
                category_color = "#FFFFFF"
            category_string = self.capitalized_category
            if self.data_dict:
                if self.data_dict.get(category_string):
                    inf.show_error_window("ERROR: The category_name you want to add already exists!")
                    return
                else:
                    category_entry = self.build_category()
                    self.data_dict[category_string] = [category_entry]
                    self.data_list.insert(len(self.data_list)-4, category_entry)
            self.add_color(category_color, category_string)
            dst.create_file(self.data_list, "Financial_Status")
        
class Movement(Category):
    def __init__(self):
        super().__init__()
        self.movement_type = ""
        self.amount = 0
        self.date = ""
        self.color_index = 0

    def build_movement_entry(self):
        category = self.capitalized_category
        movement_entry = [category, self.movement_type, self.amount, self.date]
        return movement_entry

    def process_movement_data_entry(func):
        def wrapper(self, movement_type):
            event, values = inf.add_movement_window(movement_type)
            try:
                if all(values.values()):
                        self.category_name = values['TITLE']
                        self.amount = int(values['AMOUNT'])
                        self.date = datetime.strptime(values['DATE'], "%Y/%m/%d").date()
            except ValueError:
                inf.show_error_window("Please enter only numbers for amount and date")
            func(self, movement_type)
        return wrapper

    @process_movement_data_entry
    def add_movement_entry(self, movement_type):
        self.movement_type = movement_type
        if self.category_name and self.amount and self.date:
            movement_entry = self.build_movement_entry()
                    
            if self.category_name in self.data_dict.keys():
                self.data_dict[self.category_name].append(movement_entry)
                self.assign_saved_colors(self.data_dict)
                self.update_net_balance(self.data_list)
                dst.create_file(self.data_list, "Financial_Status")
                self.category_name = ""
                self.amount = 0
                self.date = ""

class Table_Colors():
    def __init__(self):
        super().__init__()
        self.colors_dict = {}
        self.colors_list = []

    def add_color(self, color, key = ''):
        if key:
            self.colors_dict[key] = color
            dst.create_json(self.colors_dict)
        self.assign_saved_colors()
    
    def create_colors_tuples_list(self, temp_color_list, filter_action = False):
        if not filter_action:
            self.colors_list = []
            for index, color in enumerate(temp_color_list):
                self.colors_list.append([index, color, ''])
        else:
            self.filter_colors_list = []
        for index, color in enumerate(temp_color_list):
            self.filter_colors_list.append([index, color, ''])

    def assign_saved_colors(self, data_dict, opening_file = False, filter_action = False):
        if opening_file:
            self.colors_dict = dst.read_json_file()
        temporal_colors_list = []
        if data_dict and self.colors_dict:
            for key in data_dict.keys():
                if key in self.colors_dict.keys():
                    number_of_items = len(data_dict[key])
                    temporal_colors_list.extend([self.colors_dict.get(key)]*number_of_items)
        self.create_colors_tuples_list(temporal_colors_list, filter_action)

class Filter(Table_Colors):
    def __init__(self):
        super().__init__()
        self.date1 = ""
        self.date2 = ""
        self.filter_data_list = []
        self.filter_colors_list = []
        self.filter_dict = {}

    def create_filter_dictionary(self):
        for row in self.filter_data_list:
            if self.filter_dict.get(row[0]):
                self.filter_dict[row[0]].append(row)
            else:
                self.filter_dict[row[0]] = [row]

    def validate_filter_dates_entry(func):
        def wrapper(self, values):
            try:
                date1 = datetime.strptime(values['DATE1'], "%Y/%m/%d").date()
                date2 = datetime.strptime(values['DATE2'], "%Y/%m/%d").date()
                if (date1 > date.today()) or (date2 > date.today()):
                    raise Exception
                elif date2 < date1:
                    temporal_date1 = date1
                    date1 = date2
                    date2 = temporal_date1
                values = {'DATE1': date1, 'DATE2': date2}
            except ValueError:
                inf.show_error_window("Enter dates in format yyyy/mm/dd")
                return self.data_list, self.colors_list
            except Exception:
                inf.show_error_window("Do not use future dates!")
                return self.data_list, self.colors_list
            return func(self, values)
        return wrapper

    @validate_filter_dates_entry
    def filter_data(self, values):
        data_list = self.data_list
        self.date1 = values['DATE1']
        self.date2 = values['DATE2']

        if self.date1 and self.date2 and data_list:
            for row in range(0 , len(data_list)):
                row_date = data_list[row][3]
                if row_date == '':
                    continue
                else:
                    row_date = datetime.strptime(row_date, "%Y-%m-%d").date()
                    if row_date >= self.date1 and row_date <= self.date2:
                        self.filter_data_list.append(data_list[row])
            self.create_filter_dictionary()
            self.assign_saved_colors(self.filter_dict, filter_action = True)
            self.update_net_balance(self.filter_data_list, True)
            return self.filter_data_list, self.filter_colors_list

class Actions_Menu_Management(Movement, Filter):
    def __init__(self):
        super().__init__()

    def actions_management(self, event, values):
        if event == 'Add New Title':
            self.add_category_entry()
        elif event == 'Add Income':
            self.add_movement_entry("Income")
        elif event == 'Add Outcome':
            self.add_movement_entry("Outcome")
        elif event == 'Filter':
            data, colors = self.filter_data(values)
            return data, colors
        elif event == 'Clear Filter':
            self.filter_data_dict = []
            self.filter_colors_list = []
        elif event == 'Export File':
            dst.create_file(self.data_list)
        elif event == 'Import File':
            self.data_list = dst.open_file(self.data_list)
        return self.data_list, self.colors_list

class FinancialManager(Actions_Menu_Management):
    def __init__(self, header, data_list, data_dict):
        super().__init__()
        self.header = header
        self.data_dict = data_dict
        self.data_list = data_list

    def update_data_list(self):
        if self.data_dict:
            self.data_list = list(itertools.chain.from_iterable(self.data_dict.values()))

    def update_net_balance(self, data_list, filter_action = False):
        total_income = 0
        total_outcome = 0
        try:
            for row in range(0 , len(data_list)):
                title = data_list[row][1]
                total_values = data_list[row][0]
                if title == '':
                    continue
                elif title == 'Income':
                    total_income += int(data_list[row][2])
                elif title == 'Outcome':
                    total_outcome += int(data_list[row][2])
                elif total_values == 'Income:':
                    data_list[row][1] = total_income
                elif total_values == 'Outcome:':
                    data_list[row][1] = total_outcome
                elif total_values == 'Net Balance:':
                    data_list[row][1] = total_income - total_outcome
            if not filter_action:
                self.data_dict['Income:'][0][1] = total_income
                self.data_dict['Outcome:'][0][1] = total_outcome
                self.data_dict['Net Balance:'][0][1] = total_income - total_outcome
                self.update_data_list()
            else:
                self.filter_data_list = data_list
        except ValueError:
            inf.show_error_window("Grand Total could not be updated, non numeric values present, correct file and import again.")

def main():
    headings = ["Category_name", "Type", "Amount", "Date"]
    #data_dict = [["Food", "Outcome", 5500, date.today()], ["Gas", "Income", 7000, date.today()], ["Grand Total", "", 0, ""],]
    data_list, data_dict = dst.open_file(file_name = "Financial_Status")
    financial_manager = FinancialManager(headings, data_list, data_dict)
    financial_manager.assign_saved_colors(data_dict, True)

    inf.show_main_window(financial_manager)

if __name__ == '__main__':
    main()