global user_logged_in

def requires_logged_in (func):
    def wrapper (parameter):
        try:
            if user_logged_in:
                func(parameter)
            else:
                raise Exception
        except Exception:
            print("User is not authenticated")
    return wrapper

@requires_logged_in
def show_profile (name):
    print(f"Showing {name} profile")

user_logged_in = True
show_profile("Andrés")
user_logged_in = False
show_profile("Andrés")