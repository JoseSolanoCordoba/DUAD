
def change_order(list):
    last_element = list.pop(len(list)-1)
    list.append(list[0])
    list[0] = last_element
    print(list)




if __name__ == '__main__':
    first_list = ["1", "Word", "Another phrase"]
    second_list = ["2", "Some words", "number", "Character", "infinite"]


    change_order(first_list)
    change_order(second_list)