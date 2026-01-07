def print_first_word (first_word):
    print(first_word)
    print_second_word()
    print(first_word)


def print_second_word():
    print("+")


if __name__ == '__main__':
    word = "nine"
    print_first_word(word)
