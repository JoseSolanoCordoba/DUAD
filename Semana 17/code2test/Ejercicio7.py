def calculate_prime_numbers(list):
    prime_numbers = []
    for value in list:
        if is_prime_number(value):
            prime_numbers.append(value)
    return prime_numbers


def is_prime_number(number):
    factors = []
    for factor in range(2, number):
        if factor**2 > number:
            break
        if number % factor == 0:
            factors.append(factor)
       
    if not factors:
        return True
    else:
        return False

if __name__ == '__main__':
    my_list = [3, 20, 500, 12, 5, 4, 7, 11] 
    print(calculate_prime_numbers(my_list))