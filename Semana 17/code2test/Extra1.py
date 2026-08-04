def sum_elements_of_list(list):
    result = sum(list)
    return result

def average_of_list(list):
    result = sum(list)
    if len(list) != 0:
        result = result/len(list)
    return result

def max_element_of_list(list):
    result = max(list)
    return result

if __name__ == '__main__':
    my_list = [3, 20, 12, 5, 4] 
    print(sum_elements_of_list(my_list))