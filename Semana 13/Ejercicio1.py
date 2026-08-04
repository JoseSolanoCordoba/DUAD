def print_parameters(func):
    def wrapper(*args):
        print(f"These are the parameters {args}")
        result = func(*args)
        print(f'Result: {result}')
    return wrapper

@print_parameters
def any_function(expected_value, actual_value):
    return expected_value != actual_value

any_function(5, 6)