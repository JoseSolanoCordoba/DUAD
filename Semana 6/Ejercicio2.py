global_variable = "one"

def print_first_word (first_word):
    global global_variable
    global_variable = 34

if __name__ == '__main__':
    word = "nine"
    print_first_word(word)
    print(global_variable)