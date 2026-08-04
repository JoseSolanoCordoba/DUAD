import heapq
import data
import menu

#Function to display students data in good looking way
def visualize_data(students_data):
    for student_object in students_data:
        print(f"Name: {student_object.name}")
        print(f"Section: {student_object.section}")
        print(f"Spanish_grade: {student_object.spanish_grade}")
        print(f"English_grade: {student_object.english_grade}")
        print(f"Social_studies_grade: {student_object.social_studies_grade}")
        print(f"Science_grade: {student_object.science_grade}")
        print(f"Average: {student_object.average}\n")

#Top 3 calculation
def top3_calculation(students_data_list):
    students_average_list = []
    for student_object in students_data_list:
        students_average_list.append(student_object.average)
    
    top_3 = heapq.nlargest(3, enumerate(students_average_list), key=lambda x: x[1])

    print("Top 3 students are the next:\n")
    print(f"{students_data_list[top_3[0][0]].name}: {top_3[0][1]}")
    print(f"{students_data_list[top_3[1][0]].name}: {top_3[1][1]}")
    print(f"{students_data_list[top_3[2][0]].name}: {top_3[2][1]}")

    return 1

#Total average grades calculation
def total_average_grades(students_data):
    adding = 0
    for index, student_object in enumerate(students_data):
        average = (int(student_object.spanish_grade) + int(student_object.english_grade) + int(student_object.social_studies_grade) + int(student_object.science_grade))/4
        students_data[index].average = average

        adding += average
    total_average = adding/(len(students_data)+1)
    return total_average

#Function to manage other processes with more steps
def operation_management(students_data_list, action):
    if action == 2:
        total_average_grades(students_data_list)
        top3_calculation(students_data_list)
    elif action == 3:
        total_average = total_average_grades(students_data_list)
        print(f'The total average is: {total_average}')
    elif action == 4:
        data.write_csv_file('students_grades.csv', students_data_list)
    elif action == 5:
        menu.request_students_data(students_data_list, "1")
    return 0
