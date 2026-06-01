import numbers

def check_integers(func):
    def wrapper(*args):
        try:
            if not all(isinstance(value, numbers.Number) for value in args):
                raise ValueError
            else:
                result = func(*args)
                print(f'Result: {result}')
        except ValueError:
            print("Enter only numbers ")
        
    return wrapper

@check_integers
def any_function(expected_value, actual_value):
    return expected_value != actual_value

any_function(5, 6)
any_function(5, "word")