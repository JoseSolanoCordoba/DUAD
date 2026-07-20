from logic import *
from data_storage import *
import pytest

def test_add_new_data_non_numerical_amount_handling_valueerror():
    #Arrange
    table_data = []
    values = {'TITLE': 'Gas', 'AMOUNT': '20mil', 'YEAR': '2025', 'MONTH': '12', 'DAY': '10'}
    #Act
    table_data = add_new_data(table_data, values, 'Income')
    #Assert
    assert table_data == []

def test_add_new_data_empty_data_input():
    #Arrange
    table_data = []
    values = {'TITLE': '', 'AMOUNT': '', 'YEAR': '', 'MONTH': '', 'DAY': ''}
    #Act
    table_data = add_new_data(table_data, values, 'Income')
    #Assert
    assert table_data == []

def test_check_title_existence_with_empty_data_table():
    #Arrange
    table_data = []
    values = {'TITLEINPUT': 'Gas'}
    #Act
    check_title_existence(table_data, values)
    #Assert
    assert table_data == [[values['TITLEINPUT'],"","",""]]

def test_check_title_existence_with_empty_data_input():
    #Arrange
    table_data = []
    values = {'TITLEINPUT': ''}
    #Act
    check_title_existence(table_data, values)
    #Assert
    assert table_data == []

def test_update_grand_total_non_numeric_values_imported_file_valueerror():
    #Arrange
    table_data = [["Food", "Outcome", '20mil', date.today()],]
    #Act
    table_data = update_grand_total(table_data)
    #Assert
    assert table_data == [["Food", "Outcome", '20mil', date.today()],]

def test_open_file_not_exist():
    #Arrange
    file_name = "Finance"
    #Act
    data_list = open_file(file_name)
    #Assert
    assert data_list == []

