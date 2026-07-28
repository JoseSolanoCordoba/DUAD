from logic import *
from data_storage import *
import pytest
from datetime import datetime, date


headings = ["Category_name", "Type", "Amount", "Date"]
totals_headings = ["Total_Summary", "Amount"]

def test_add_category_entry_with_empty_input_exception_management():
    #Arrange
    data_list = []
    data_dict = {}
    totals_list = []
    financial_manager = FinancialManager(headings, data_list, data_dict, totals_headings, totals_list)
    values = {'TITLEINPUT': '', 'COLOR': ''}
    #Act
    financial_manager.add_category_entry(values)
    #Assert
    assert financial_manager.data_list == []

def test_add_category_entry_normal_entry_in_initial_empty_data():
    #Arrange
    data_list = []
    data_dict = {}
    totals_list = []
    financial_manager = FinancialManager(headings, data_list, data_dict, totals_headings, totals_list)
    values = {'TITLEINPUT': 'Gas', 'COLOR': '#008000'}
    #Act
    financial_manager.add_category_entry(values)
    #Assert
    assert financial_manager.data_list == [['Gas', '', '', '']]
    assert financial_manager.data_dict == {'Gas': [['Gas', '', '', '']]}
    assert financial_manager.totals_list == [['Income:', 0], ['Outcome:', 0], ['Net Balance:', 0]]

def test_add_category_entry_with_repeated_category():
    #Arrange
    data_list = [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]
    data_dict = {'Gas': [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]}
    totals_list = [['Income:', 0], ['Outcome:', 2000], ['Net Balance:', -2000]]
    financial_manager = FinancialManager(headings, data_list, data_dict, totals_headings, totals_list)
    values = {'TITLEINPUT': 'Gas', 'COLOR': '#008000'}
    #Act
    financial_manager.add_category_entry(values)
    #Assert
    assert financial_manager.data_list == [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]
    assert financial_manager.data_dict == {'Gas': [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]}
    assert financial_manager.totals_list == [['Income:', 0], ['Outcome:', 2000], ['Net Balance:', -2000]]

def test_add_movement_entry_with_empty_input_exception_management():
    #Arrange
    data_list = [['Gas', '', '', '']]
    data_dict = {'Gas': [['Gas', '', '', '']]}
    totals_list = [['Income:', 0], ['Outcome:', 0], ['Net Balance:', 0]]
    financial_manager = FinancialManager(headings, data_list, data_dict, totals_headings, totals_list)
    values = {'TITLE': '', 'AMOUNT': '', 'DATE': ''}
    #Act
    financial_manager.add_movement_entry("Outcome", values)
    #Assert
    assert financial_manager.data_list == [['Gas', '', '', '']]
    assert financial_manager.data_dict == {'Gas': [['Gas', '', '', '']]}
    assert financial_manager.totals_list == [['Income:', 0], ['Outcome:', 0], ['Net Balance:', 0]]

def test_add_movement_entry_with_normal_input_existing_category():
    #Arrange
    data_list = [['Gas', '', '', '']]
    data_dict = {'Gas': [['Gas', '', '', '']]}
    totals_list = [['Income:', 0], ['Outcome:', 0], ['Net Balance:', 0]]
    financial_manager = FinancialManager(headings, data_list, data_dict, totals_headings, totals_list)
    values = {'TITLE': 'Gas', 'AMOUNT': '4000', 'DATE': '2021/10/12'}
    #Act
    financial_manager.add_movement_entry("Outcome", values)
    #Assert
    assert financial_manager.data_list == [['Gas', '', '', ''], ['Gas', 'Outcome', 4000, date(2021,10,12)]]
    assert financial_manager.data_dict == {'Gas': [['Gas', '', '', ''], ['Gas', 'Outcome', 4000, date(2021,10,12)]]}
    assert financial_manager.totals_list == [['Income:', 0], ['Outcome:', 4000], ['Net Balance:', -4000]]

def test_add_movement_entry_with_non_previous_existent_category():
    #Arrange
    data_list = [['Food', '', '', '']]
    data_dict = {'Food': [['Food', '', '', '']]}
    totals_list = [['Income:', 0], ['Outcome:', 0], ['Net Balance:', 0]]
    financial_manager = FinancialManager(headings, data_list, data_dict, totals_headings, totals_list)
    values = {'TITLE': 'Gas', 'AMOUNT': '4000', 'DATE': '2021/10/12'}
    #Act
    financial_manager.add_movement_entry("Outcome", values)
    #Assert
    assert financial_manager.data_list == [['Food', '', '', '']]
    assert financial_manager.data_dict == {'Food': [['Food', '', '', '']]}
    assert financial_manager.totals_list == [['Income:', 0], ['Outcome:', 0], ['Net Balance:', 0]]

def test_add_movement_entry_with_incorrect_dates_format_exception_management():
    #Arrange
    data_list = [['Gas', '', '', '']]
    data_dict = {'Gas': [['Gas', '', '', '']]}
    totals_list = [['Income:', 0], ['Outcome:', 0], ['Net Balance:', 0]]
    financial_manager = FinancialManager(headings, data_list, data_dict, totals_headings, totals_list)
    values = {'TITLE': 'Gas', 'AMOUNT': '4000', 'DATE': 'dosmilveinteerwr3r35#&'}
    #Act
    financial_manager.add_movement_entry("Outcome", values)
    #Assert
    assert financial_manager.data_list == [['Gas', '', '', '']]
    assert financial_manager.data_dict == {'Gas': [['Gas', '', '', '']]}
    assert financial_manager.totals_list == [['Income:', 0], ['Outcome:', 0], ['Net Balance:', 0]]

def test_filter_data_with_incorrect_dates_format_exception_management():
    #Arrange
    data_list = [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]
    data_dict = {'Gas': [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]}
    totals_list = [['Income:', 0], ['Outcome:', 2000], ['Net Balance:', -2000]]
    financial_manager = FinancialManager(headings, data_list, data_dict, totals_headings, totals_list)
    values = {'DATE1': '2021/09/10', 'DATE2': 'dosmilveinteerwr3r35'}
    #Act
    financial_manager.filter_data(values)
    #Assert
    assert financial_manager.data_list == [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]
    assert financial_manager.data_dict == {'Gas': [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]}
    assert financial_manager.totals_list == [['Income:', 0], ['Outcome:', 2000], ['Net Balance:', -2000]]

def test_filter_data_with_future_datesclea_exception_management():
    #Arrange
    data_list = [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]
    data_dict = {'Gas': [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]}
    totals_list = [['Income:', 0], ['Outcome:', 2000], ['Net Balance:', -2000]]
    financial_manager = FinancialManager(headings, data_list, data_dict, totals_headings, totals_list)
    values = {'DATE1': '2027/09/10', 'DATE2': '2027/10/12'}
    #Act
    financial_manager.filter_data(values)
    #Assert
    assert financial_manager.data_list == [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]
    assert financial_manager.data_dict == {'Gas': [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]}
    assert financial_manager.totals_list == [['Income:', 0], ['Outcome:', 2000], ['Net Balance:', -2000]]

def test_open_file_non_existent_file():
    #Arrange
    data_list = [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]
    data_dict = {'Gas': [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]}
    totals_list = [['Income:', 0], ['Outcome:', 2000], ['Net Balance:', -2000]]
    list_of_data, dict_of_data, list_of_totals = open_file("Financial_file", data_list, data_dict, totals_list)
    #Assert
    assert list_of_data == data_list
    assert dict_of_data == data_dict
    assert list_of_totals == totals_list

def test_read_json_file_non_existent_file():
    #Arrange
    colors_dict = {
    "Gas": "#008000"
    }
    #Act
    dict_of_colors = read_json_file("Config_file", colors_dict)
    #Assert
    assert dict_of_colors == colors_dict

def test_assign_saved_colors_normal_data():
    #Arrange
    data_list = [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]
    data_dict = {'Gas': [['Gas', '', '', ''], ['Gas', 'Outcome', '2000', '2021-12-10']]}
    totals_list = [['Income:', 0], ['Outcome:', 2000], ['Net Balance:', -2000]]
    financial_manager = FinancialManager(headings, data_list, data_dict, totals_headings, totals_list)
    #Act
    financial_manager.assign_saved_colors(data_dict, True)
    #Assert
    assert financial_manager.colors_list == [[0, "#008000", ''], [1, "#008000", '']]
