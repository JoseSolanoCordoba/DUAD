import menu 

#Main function
def main():

    try:
        menu.request_students_data() #Calling menu to show to user
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()


