import numbers

def bubble_sort (list):
    for outer_index in range(len(list)):
        for i in range(len(list)-1-outer_index):
            actual_element = list[i]
            next_element = list[i+1]
            if list[i]>list[i+1]:
                list[i+1] = actual_element
                list[i] = next_element
    return list

def check_list (list):
    if all(isinstance(val, numbers.Number) for val in list) and list:
        print(f"Reordered list: \n{bubble_sort(list)}")
    else:
        print("All the items must be numbers and not empty lists admitted")
    
#list = [3, 23, 34, 9, 2]
#list = []
list = [3, 23, 34, 9, "word"]
check_list(list)