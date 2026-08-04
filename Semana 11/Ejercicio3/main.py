import menu 

#Main function
def main():

    try:
        students_grades_info = []
        getting_data = input("Do you want to enter students data (1) or import existing csv file (any key)?\n")
        menu.request_students_data(students_grades_info, getting_data) #Calling menu to show to user
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()


