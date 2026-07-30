from datetime import datetime, date
import itertools
import interface as inf
import data_storage as dst


class Category:
    def __init__(self):
        super().__init__()
        self.category_name = ""
        self.title = ""
        self.categories_dict = {}

    @property
    def capitalized_category(self):
        self.category_name = self.category_name.capitalize()
        return self.category_name

    def build_initial_data(self):
        self.summary_list = [['Income:',0], ['Outcome:',0], ['Net Balance:',0]]
        
    def add_category_entry(self, values = {}):
        if not values:
            event, values = inf.add_category_name_window()
        self.category_name = values['TITLEINPUT']
        if self.category_name:
            category_color = values['COLOR']
            if not category_color:
                category_color = "#FFFFFF"
            category_string = self.capitalized_category
            if not self.categories_dict and not self.movements_list and not self.summary_list:
                self.build_initial_data()
            if category_string in self.categories_dict.keys():
                inf.show_error_window("ERROR: The category_name you want to add already exists!")
                return
            else:
                self.categories_dict[category_string] = []
            self.add_color(category_color, category_string)
            dst.create_file([self.header] + self.movements_list + [self.summary_headings] + self.summary_list, "Financial_Status")
        
class Movement(Category):
    def __init__(self):
        super().__init__()
        self.movement_type = ""
        self.amount = 0
        self.date = ""
        self.color_index = 0

    def build_movement_entry(self):
        category = self.capitalized_category
        movement_entry = [self.title, , self.category, self.movement_type, self.amount, self.date]
        return movement_entry

    def process_movement_data_entry(func):
        def wrapper(self, movement_type, values = {}):
            if not values:
                event, values = inf.add_movement_window(movement_type)
            try:
                self.title = values['TITLE']
                self.category_name = values['CATEGORY']
                self.amount = int(values['AMOUNT'])
                temporal_date = values['DATE']
                if temporal_date == 'dd/mm/yyyy' or temporal_date == '':
                    self.date = date.today()
                else:
                    self.date = datetime.strptime(values['DATE'], "%d/%m/%Y").date()
                if not self.category_name and self.amount and self.date:
                    raise Exception
            except ValueError:
                inf.show_error_window("Please enter every item, numbers for amount and date format (yyyy/mm/dd)")
                return wrapper
            except Exception:
                inf.show_error_window("Please enter a category")
                return wrapper
            func(self, movement_type)
        return wrapper

    @process_movement_data_entry
    def add_movement_entry(self, movement_type, values = {}):
        self.movement_type = movement_type
        movement_entry = self.build_movement_entry()
        try:
            if self.category_name in self.categories_dict:
                self.categories_dict[self.category_name].append(movement_entry)
                self.update_movements_list()
                self.assign_saved_colors(self.categories_dict)
                self.update_net_balance(self.movements_list)
                dst.create_file([self.header] + self.movements_list + [self.summary_headings] + self.summary_list, "Financial_Status")
            else:
                raise Exception
        except Exception:
            inf.show_error_window("Movement entry can not be entered:\n(The category of movement has not been created previously)")
        self.category_name = ""
        self.amount = 0
        self.date = ""
        

class Table_Colors():
    def __init__(self):
        super().__init__()
        self.colors_dict = {}
        self.colors_list = []

    def add_color(self, color, key_category = ''):
        if key_category:
            self.colors_dict[key_category] = color
            dst.create_json(self.colors_dict)

    def create_colors_tuples_list(self, temp_color_list, filter_action = False):
        if not filter_action:
            self.colors_list = []
            for index, color in enumerate(temp_color_list):
                self.colors_list.append([index, color, ''])
        else:
            self.filter_colors_list = []
        for index, color in enumerate(temp_color_list):
            self.filter_colors_list.append([index, color, ''])

    def assign_saved_colors(self, category_dict, opening_file = False, filter_action = False):
        if opening_file:
            self.colors_dict = dst.read_json_file("Colors_Config", self.colors_dict)
        temporal_colors_list = []
        if category_dict and self.colors_dict:
            for key_title in category_dict.keys():
                if key_title in self.colors_dict.keys():
                    number_of_items = len(category_dict.get(key_title))
                    temporal_colors_list.extend([self.colors_dict.get(key_title)]*number_of_items)
                else: 
                    number_of_items = len(category_dict.get(key_title))
                    temporal_colors_list.extend(["#FFFFFF"]*number_of_items)
            self.create_colors_tuples_list(temporal_colors_list, filter_action)

class Filter(Table_Colors):
    def __init__(self):
        super().__init__()
        self.date1 = ""
        self.date2 = ""
        self.filter_movements_list = []
        self.filter_colors_list = []
        self.filter_dict = {}
        self.filter_summary_list = []

    def create_filter_dictionary(self):
        for row in self.filter_movements_list:
            if self.filter_dict.get(row[0]):
                self.filter_dict[row[0]].append(row)
            else:
                self.filter_dict[row[0]] = [row]

    def validate_filter_dates_entry(func):
        def wrapper(self, values):
            try:
                date1 = datetime.strptime(values['DATE1'], "%d/%m/%Y").date()
                date2 = datetime.strptime(values['DATE2'], "%d/%m/%Y").date()
                if (date1 > date.today()) or (date2 > date.today()):
                    raise Exception
                elif date2 < date1:
                    temporal_date1 = date1
                    date1 = date2
                    date2 = temporal_date1
                values = {'DATE1': date1, 'DATE2': date2}
            except ValueError:
                inf.show_error_window("Enter dates in format yyyy/mm/dd")
                return self.movements_list, self.summary_list, self.colors_list
            except Exception:
                inf.show_error_window("Do not use future dates!")
                return self.movements_list, self.summary_list, self.colors_list
            return func(self, values)
        return wrapper

    @validate_filter_dates_entry
    def filter_data(self, values):
        movements_list = self.movements_list
        self.date1 = values['DATE1']
        self.date2 = values['DATE2']

        if self.date1 and self.date2 and movements_list:
            for row in range(0 , len(movements_list)):
                row_date = movements_list[row][3]
                if row_date == '':
                    continue
                else:
                    row_date = datetime.strptime(row_date, "%Y-%m-%d").date()
                    if row_date >= self.date1 and row_date <= self.date2:
                        self.filter_movements_list.append(movements_list[row])
            self.create_filter_dictionary()
            self.assign_saved_colors(self.filter_dict, filter_action = True)
            self.update_net_balance(self.filter_movements_list, True)
            return self.filter_movements_list, self.filter_summary_list, self.filter_colors_list

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
            return self.filter_data(values)
        elif event == 'Clear Filter':
            self.filter_movements_list = []
            self.filter_colors_list = []
            self.filter_dict = {}
        elif event == 'Export File':
            dst.create_file([self.header] + self.movements_list + [self.totals_headings] + self.summary_list)
        elif event == 'Import File':
            dst.create_file([self.header] + self.movements_list + [self.totals_headings] + self.summary_list, "Backup_file")
            self.movements_list, self.categories_dict, self.summary_list = dst.open_file(input_list = self.movements_list, input_dict= self.categories_dict, input_summary_list = self.summary_list)
            self.assign_saved_colors(self.categories_dict)
        return self.movements_list, self.summary_list, self.colors_list

class FinancialManager(Actions_Menu_Management):
    def __init__(self, header, categories_dict, movements_list, summary_headings, summary_list):
        super().__init__()
        self.header = header
        self.categories_dict = categories_dict
        self.movements_list = movements_list
        self.summary_headings = summary_headings
        self.summary_list = summary_list

    def update_movements_list(self):
        if self.categories_dict:
            self.movements_list = list(itertools.chain.from_iterable(self.categories_dict.values()))

    def update_net_balance(self, movements_list, filter_action = False):
        total_income = 0
        total_outcome = 0
        try:
            for row in range(0 , len(movements_list)):
                category = movements_list[row][1]
                if category == 'Income':
                    total_income += int(movements_list[row][2])
                elif category == 'Outcome':
                    total_outcome += int(movements_list[row][2])
            if not filter_action:
                self.summary_list = []
                self.summary_list = [['Income:', total_income], ['Outcome:', total_outcome], ['Net Balance:', total_income - total_outcome]]
            else:
                self.filter_summary_list = []
                self.filter_summary_list = [['Income:', total_income], ['Outcome:', total_outcome], ['Net Balance:', total_income - total_outcome]]
        except ValueError:
            inf.show_error_window("Grand Total could not be updated, non numeric values present, correct file and import again.")

def main():
    headings = ["Category_name", "Type", "Amount", "Date"]
    summary_headings = ["Total_Summary", "Amount"]
    categories_dict, movements_list, summary_list = dst.open_file(file_name = "Financial_Status")
    financial_manager = FinancialManager(headings, categories_dict, movements_list, summary_headings, summary_list)
    financial_manager.assign_saved_colors(categories_dict, True)

    inf.show_main_window(financial_manager)

if __name__ == '__main__':
    main()