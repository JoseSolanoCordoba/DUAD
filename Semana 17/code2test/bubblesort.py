def bubble_sort (list):
    for outer_index in range(len(list)):
        for i in range(len(list)-1-outer_index):
            actual_element = list[i]
            next_element = list[i+1]
            if list[i]>list[i+1]:
                list[i+1] = actual_element
                list[i] = next_element
    return list

list = [3, 23, 34, 9, 2]
print(bubble_sort(list))
