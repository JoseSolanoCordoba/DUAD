import heapq
import data
import menu

#Function to display students data in good looking way
def visualize_data(students_data):
    for i in range(len(students_data)):
        for key, value in students_data[i].items():
            if key == "science_grade": 
                print(f"{key}: {value}\n")
            else:
                print(f"{key}: {value}")

#Top 3 calculation
def top3_calculation(average_per_student_dict):
    top_3 = heapq.nlargest(3, average_per_student_dict.keys())
    print("Top 3 students are the next:\n")
    for value in top_3:
        print(f'{average_per_student_dict[value]}:{value}')
    return 1

#Total average grades calculation
def total_average_grades(students_data):
    average_grades_all_students_dict = {}
    adding = 0
    for i in range(len(students_data)):
        average = (int(students_data[i]["spanish_grade"]) + int(students_data[i]["english_grade"]) + int(students_data[i]["social_studies_grade"]) + int(students_data[i]["science_grade"]))/4
        average_grades_all_students_dict[average] = students_data[i]["name"]

        adding += average
    total_average = adding/(i+1)

    return average_grades_all_students_dict, total_average

#Function to manage other processes with more steps
def operation_management(students_data_dict_list, action):
    if action == 2:
        average_per_student_dict, total_average = total_average_grades(students_data_dict_list)
        top3_calculation(average_per_student_dict)
    elif action == 3:
        average_per_student_dict, total_average = total_average_grades(students_data_dict_list)
        print(f'The total average is: {total_average}')
    elif action == 4:
        data.write_csv_file('students_grades.csv', students_data_dict_list)
    elif action == 5:
        menu.request_students_data(students_data_dict_list, 1)
    return 0
