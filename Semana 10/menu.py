import actions
import data

#Function to request student name
def request_name():
    name = ""
    while(name == ""):
        try:
            name = input("Please enter the name:\n")
            if name.isdigit():
                raise ValueError("The name can´t be a number")
            
        except ValueError as ex:
            print(f"{ex}\n")
            print("Enter a valid name")  
            name = ""
    return name

#Function to request section
def request_section():
    section = ""
    while(section == ""):
        section = input(f"Enter your section: ")
    return section

#Function to request spanish grade
def request_spanish_grade():
    spanish_grade = 0
    while(spanish_grade == 0):
        try:
            spanish_grade = int(input(f"Enter your spanish grade: "))
            if spanish_grade<0 or spanish_grade>100:
                raise ValueError
        except ValueError as ex:
            print(f"{ex}\n")
            print("Enter a valid number between 0 and 100")  
            spanish_grade = 0
    return spanish_grade

#Function to request english grade
def request_english_grade():
    english_grade = 0
    while(english_grade == 0):
        try:
            english_grade = int(input(f"Enter your english grade: "))
            if english_grade<0 or english_grade>100:
                raise ValueError
        except ValueError as ex:
            print(f"{ex}\n")
            print("Enter a valid number between 0 and 100")  
            english_grade = 0
    return english_grade

#Function to request social studies grade
def request_social_studies_grade():
    social_studies_grade = 0
    while(social_studies_grade == 0):
        try:
            social_studies_grade = int(input(f"Enter your social studies grade: "))
            if social_studies_grade<0 or social_studies_grade>100:
                raise ValueError
        except ValueError as ex:
            print(f"{ex}\n")
            print("Enter a valid number between 0 and 100")  
            social_studies_grade = 0
    return social_studies_grade

#Function to request science grade
def request_science_grade():
    science_grade = 0
    while(science_grade == 0):
        try:
            science_grade = int(input(f"Enter your science grade: "))
            if science_grade<0 or science_grade>100:
                raise ValueError
        except ValueError as ex:
            print(f"{ex}\n")
            print("Enter a valid number between 0 and 100")  
            science_grade = 0
    return science_grade

#Function to develop different action depending on user selected option once students data was entered
def call_actions(students_data_list):
    print("\nNow you have entered all students data, you can choose the following options:\n")
    selection= 0
    while(True):
        try:
            selection = int(input("Choose an option:\n1: Show all students data\n2: Show the top 3 average grades students\n3: Calculate the total average\n4: Export actual data to csv file format\n0: To exit the program\n"))
            if selection == 0:
                exit()
            elif selection not in {1,2,3,4}:
                raise ValueError
            elif selection == 1:
                actions.visualize_data(students_data_list)
            else:
                actions.operation_management(students_data_list, selection)
        except ValueError as ex:
            print("Choose a valid option number:1 thru 5")
    
    return 0

#Function to request students data
def request_students_data():
    students_grades_info = []
    getting_data = input("Do you want to enter students data (1) or import existing csv file (any key)?\n")
    if getting_data =="1":
        #students_grades_info = [{'name': 'John', 'section': '34r', 'spanish_grade': 100, 'english_grade': 20, 'social_studies_grade': 30, 'science_grade': 40}, {'name': 'Wer', 'section': '12r', 'spanish_grade': 90, 'english_grade': 62, 'social_studies_grade': 83, 'science_grade': 74}, {'name': 'Jay', 'section': '10b', 'spanish_grade': 100, 'english_grade': 100, 'social_studies_grade': 100, 'science_grade': 100}, {'name': 'Gaby', 'section': '34a', 'spanish_grade': 90, 'english_grade': 90, 'social_studies_grade': 90, 'science_grade': 90}]
        while(True):
            student_data = {"name": request_name(), "section": request_section(), "spanish_grade": request_spanish_grade(), "english_grade": request_english_grade(), "social_studies_grade": request_social_studies_grade(), "science_grade": request_science_grade()}
            students_grades_info.append(student_data)
            addingmore = input(f"Do you want to add another student? 1:yes, any key for no\n")
            if addingmore!="1":
                break
    else:
        students_grades_info = data.import_csv_file()

    #If list is not empty continue with the program
    if students_grades_info:
        call_actions(students_grades_info)
    else:
        request_students_data()
        


        #student_data(request_name(), request_spanish_grade(), request_english_grade(), request_social_studies_grade(), request_science_grade())
