from datetime import date

class User():
    name: str
    date_of_birth: date

    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today_date = date.today()
        return (today_date.year - self.date_of_birth.year) - ((today_date.month, today_date.day)<(self.date_of_birth.month, self.date_of_birth.day))

def check_majority (func):
    def wrapper(user):
        try:
            if user.age < 18:
                raise Exception
            else:
                func(user)
        except Exception:
            print("User age is less than 18")
    return wrapper

@check_majority
def empty_function1(user):
    pass

@check_majority
def empty_function2(user):
    pass

user1 = User("Andrés", date(1993, 6, 2))
print (f'User 1 age: {user1.age}')
user2 = User("José", date(2009, 3, 2))
print (f'User 2 age: {user2.age}')

empty_function1(user1)  #No exception raised
empty_function1(user2)  #Exception
empty_function2(user2)  #Exception