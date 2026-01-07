def reorder_songs(path):
    with open(path, 'r', encoding='utf-8') as my_file:
        my_file = my_file.readlines()
        my_file.sort()
    return my_file


def create_new_file(songs_list):
    path = "..\\Curso Lyfter\\Semana 8\\reordered_songs.txt"
    with open(path, 'w') as new_file:
        new_file.writelines(songs_list)


def main():
    path = "..\\Curso Lyfter\\Semana 8\\Songs.txt"
    try:
        reordered_songs = reorder_songs(path)
        create_new_file(reordered_songs)
    except Exception as ex:
            print(ex)
            exit()

if __name__ == '__main__':
    main()
    