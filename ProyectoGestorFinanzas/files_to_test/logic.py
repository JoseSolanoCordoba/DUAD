from datetime import datetime, date
import itertools
import data_storage as dst
import interface as inf

FILE_NAME = "Financial_Status.csv"
COLORS_CONFIG = "Colors_Config.json"
INCOME = "Income"
OUTCOME = "Outcome"
ADD_INCOME = "Add " + INCOME
ADD_OUTCOME = "Add " + OUTCOME
NET_BALANCE = "NET_BALANCE"
HEADINGS = ["Date", "Title", "Amount", "Category", "Type"]
SUMMARY_HEADINGS = ["Total_Summary", "Amount"]

class Category():
    def __init__(self):
        self.category_name = ""
        self.category_color = ""

    def build_initial_data(self):
        summary_list = [[INCOME,0], [OUTCOME,0], ['NET_BALANCE:',0]]
        return summary_list
        
    def add_category_entry(self, category_dict, values = {}):
        if not values:
            event, values = inf.add_category_name_window()
        self.category_name = values['CATEGORYINPUT']
        if self.category_name:
            self.category_name = self.category_name.capitalize()
        if self.category_name:
            self.category_color = values['COLOR']
            if not self.category_color:
                self.category_color = "#FFFFFF"
            if category_dict.get(self.category_name):
                inf.show_error_window("ERROR: The category_name you want to add already exists!")
            else:
                category_dict[self.category_name] = []
            return category_dict

class Movement():
    def __init__(self):
        self.title = ""
        self.movement_type = ""
        self.amount = 0
        self.date = ""
        self.category_object = Category()
        self.colors_object = Table_Colors()
        
    def build_movement_entry(self):
        movement_entry = [self.date, self.title,  self.amount, self.category_object.category_name, self.movement_type]
        return movement_entry

    def process_movement_data_entry(func):
        def wrapper(self, movement_type, categories_dict, values = {}):
            if not values:
                event, values = inf.add_movement_window(movement_type)
            try:
                self.title = values['TITLE']
                if not self.title:
                    raise ValueError("Empty title")
                
                self.category_object.category_name = values['CATEGORY']
                if self.category_object.category_name:
                    self.category_object.category_name = self.category_object.category_name.capitalize()

                self.movement_type = movement_type

                self.amount = int(values['AMOUNT'])
                if self.amount <= 0:
                    raise ValueError("Invalid amount")
                
                temporal_date = values['DATE']
                if temporal_date == 'dd/mm/yyyy' or temporal_date == '':
                    self.date = date.today()
                else:
                    self.date = datetime.strptime(values['DATE'], "%d/%m/%Y").date()
                    if self.date > date.today():
                        raise ValueError("Future date")
                    
                if not self.category_object.category_name and self.amount and self.date:
                    raise ValueError("Empty Category")
                
            except ValueError as ve:
                if str(ve) == "Empty Category":
                    inf.show_error_window("Please enter a category")
                elif str(ve) == "Future date":
                    inf.show_error_window("Do not use future dates")
                elif str(ve) == "Invalid amount":
                    inf.show_error_window("Enter only positive numbers major to zero for amount")
                else:
                    inf.show_error_window("Please enter every item, numbers for amount and date format (dd/mm/yyyy)")
                return categories_dict
            except TypeError:
                inf.show_error_window("Enter a value for amount")
                return categories_dict
            return func(self, movement_type, categories_dict)
        return wrapper

    @process_movement_data_entry
    def add_movement_entry(self, movement_type, categories_dict, values = {}):
        movement_entry = self.build_movement_entry()
        try:
            if self.category_object.category_name in categories_dict:
                categories_dict[self.category_object.category_name].append(movement_entry)
            else:
                raise Exception
        except Exception:
            inf.show_error_window("Movement entry can not be entered:\n(The category of movement has not been created previously)")
        self.category_name = ""
        self.amount = 0
        self.date = ""
        return categories_dict
        
class Table_Colors():
    def __init__(self):
        self.colors_dict = {}
        self.colors_list = []
        self.filter_object = Filter()

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
            self.filter_object.filter_colors_list = []
        for index, color in enumerate(temp_color_list):
            self.filter_object.filter_colors_list.append([index, color, ''])

    def assign_saved_colors(self, category_dict, opening_file = False, filter_action = False):
        if opening_file:
            self.colors_dict = dst.read_json_file(COLORS_CONFIG, self.colors_dict)
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

class Filter():
    def __init__(self):
        self.date1 = ""
        self.date2 = ""
        self.filter_movements_list = []
        self.filter_summary_list = []
        self.filter_colors_list = []
        self.filter_dict = {}

    def create_filter_dictionary(self):
        for row in self.filter_movements_list:
            if self.filter_dict.get(row[3]):
                self.filter_dict[row[3]].append(row)
            else:
                self.filter_dict[row[3]] = [row]

    def validate_filter_dates_entry(func):
        def wrapper(self, movements_list, values):
            try:
                date1 = datetime.strptime(values['DATE1'], "%d/%m/%Y").date()
                date2 = datetime.strptime(values['DATE2'], "%d/%m/%Y").date()
                if (date1 > date.today()) or (date2 > date.today()):
                    raise ValueError("Future Error")
                elif date2 < date1:
                    temporal_date1 = date1
                    date1 = date2
                    date2 = temporal_date1
                values = {'DATE1': date1, 'DATE2': date2}
            except ValueError as ve:
                if str(ve) == "Future Error":
                    inf.show_error_window("Do not use future dates!")
                else:
                    inf.show_error_window("Enter dates in format dd/mm/yyyy")
                return None
            return func(self, movements_list, values)
        return wrapper

    @validate_filter_dates_entry
    def filter_data(self, movements_list, values):
        self.date1 = values['DATE1']
        self.date2 = values['DATE2']

        if self.date1 and self.date2 and movements_list:
            for row in range(0 , len(movements_list)):
                row_date = movements_list[row][0]
                if row_date == '':
                    continue
                else:
                    row_date = datetime.strptime(row_date, "%Y-%m-%d").date()
                    if row_date >= self.date1 and row_date <= self.date2:
                        self.filter_movements_list.append(movements_list[row])
            self.create_filter_dictionary()
            return True

class FinancialManager():
    def __init__(self, categories_dict, movements_list, summary_list):
        self.header = HEADINGS
        self.categories_dict = categories_dict
        self.movements_list = movements_list
        self.summary_headings = SUMMARY_HEADINGS
        self.summary_list = summary_list
        self.category_object = Category()
        self.movement_object = Movement()
        self.colors_object = Table_Colors()
        self.filter_object = Filter()
        if not self.categories_dict and not self.movements_list and not self.summary_list:
            self.summary_list = self.category_object.build_initial_data()
    
    def actions_management(self, event, values):
            if event == 'Add New Category':
                self.categories_dict = self.category_object.add_category_entry(self.categories_dict)
                self.colors_object.add_color(self.category_object.category_color, self.category_object.category_name)
            elif event == ADD_INCOME:
                self.categories_dict = self.movement_object.add_movement_entry(INCOME, self.categories_dict)
                self.colors_object.assign_saved_colors(self.categories_dict)
                self.update_movements_list()
                self.update_net_balance(self.movements_list)
            elif event == ADD_OUTCOME:
                self.categories_dict = self.movement_object.add_movement_entry(OUTCOME, self.categories_dict)
                self.colors_object.assign_saved_colors(self.categories_dict)
                self.update_movements_list()
                self.update_net_balance(self.movements_list)
            elif event == 'Filter':
                if self.filter_object.filter_data(self.movements_list, values):
                    self.colors_object.assign_saved_colors(self.filter_object.filter_dict, filter_action = True)
                    self.update_net_balance(self.filter_object.filter_movements_list, True)
                    return self.filter_object.filter_movements_list, self.filter_object.filter_summary_list, self.filter_object.filter_colors_list
            elif event == 'Clear Filter':
                self.filter_object.date1 = ''
                self.filter_object.date2 = ''
                self.filter_object.filter_movements_list = []
                self.filter_object.filter_summary_list = []
                self.filter_object.filter_colors_list = []
                self.filter_object.filter_dict = {}
            elif event == 'Export File':
                dst.create_file([self.header] + self.movements_list + [self.summary_headings] + self.summary_list)
            elif event == 'Import File':
                dst.create_file([self.header] + self.movements_list + [self.summary_headings] + self.summary_list, "Backup_file.csv")
                self.categories_dict, self.movements_list, self.summary_list = dst.open_file(input_list = self.movements_list, input_dict= self.categories_dict, input_summary_list = self.summary_list)
                self.colors_object.assign_saved_colors(self.categories_dict)
            return self.movements_list, self.summary_list, self.colors_object.colors_list
            
    def update_movements_list(self):
        if self.categories_dict:
            self.movements_list = list(itertools.chain.from_iterable(self.categories_dict.values()))

    def build_initial_data(self):
        self.summary_list = [[INCOME,0], [OUTCOME,0], ['NET_BALANCE:',0]]

    def update_net_balance(self, movements_list, filter_action = False):
        total_income = 0
        total_outcome = 0
        try:
            for row in range(0 , len(movements_list)):
                transaction_type = movements_list[row][4]
                if transaction_type == INCOME:
                    total_income += int(movements_list[row][2])
                elif transaction_type == OUTCOME:
                    total_outcome += int(movements_list[row][2])
            if not filter_action:
                self.summary_list = []
                self.summary_list = [[INCOME, total_income], [OUTCOME, total_outcome], [NET_BALANCE, total_income - total_outcome]]
            else:
                self.filter_object.filter_summary_list = []
                self.filter_object.filter_summary_list = [[INCOME, total_income], [OUTCOME, total_outcome], [NET_BALANCE, total_income - total_outcome]]
        except ValueError:
            inf.show_error_window("Grand Total could not be updated, non numeric values present, correct file and import again.")

def main():
    categories_dict, movements_list, summary_list = dst.open_file(file_name = FILE_NAME)
    financial_manager = FinancialManager(categories_dict, movements_list, summary_list)
    financial_manager.colors_object.assign_saved_colors(categories_dict, True)

    inf.show_main_window(financial_manager)

if __name__ == '__main__':
    main()