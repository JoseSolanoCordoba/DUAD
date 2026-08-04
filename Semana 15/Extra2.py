def bubble_sort_steps (list):
    interchange = 0
    iterations = 0
    for outer_index in range(len(list)):
        for i in range(len(list)-1-outer_index):
            actual_element = list[i]
            next_element = list[i+1]
            if list[i]>list[i+1]:
                list[i+1] = actual_element
                list[i] = next_element
                interchange += 1
        iterations += 1
    return list, interchange, iterations

list = [3, 23, 34, 9, 2]
list, inter, ite = bubble_sort_steps(list)
print(f"Reordered list: {list}\nIterations: {ite}\nInterchanges: {inter}")