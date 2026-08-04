import datetime
import numbers

def validate_numbers (func):
    def wrapper (*args):
        try:
            if all(isinstance(item, numbers.Number) for item in args):
                print("Multiplying numbers")
                result = func(*args)
                return result
            else:
                raise Exception
        except Exception:
            print("Enter numbers only")
    return wrapper

def log_call (func):
    def wrapper (*args):
        result = func(*args)
        print(f"func:{func.__name__} - args: {args} - [{datetime.datetime.now()}] - Result: {result}")
    return wrapper

@log_call
@validate_numbers
def multiply (number1, number2):
    return number1*number2

multiply(1,3)
