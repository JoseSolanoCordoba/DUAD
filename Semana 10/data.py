import csv
import os

#Import existing csv file with desired students data
def import_csv_file():
    list_of_students_info = []
    actual_path = os.getcwd()
    try:
        file_name = input("Enter the file name you want to import, assuming it is located in this working path:\n")
        full_path = actual_path+ "\\" +file_name
        with open(full_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                list_of_students_info.append(row)
    except FileNotFoundError:
        print("The file you look for does not exist, enter the correct path or choose (1) to go to the previous menu")
    return list_of_students_info

#Create csv file with actual students data
def write_csv_file(file_path, data):
    fieldnames = [
        'name',
        'section', 
        'spanish_grade', 
        'english_grade', 
        'social_studies_grade', 
        'science_grade',]
    
    with open(file_path, 'w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    return 0

