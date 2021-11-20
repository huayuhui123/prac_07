"""..."""
# Copy your first assignment to this file, then update it to use the Album class

from album import Album
import csv
from operator import attrgetter

menu = """Menu:
L - List all albums
A - Add new album
M - Mark an album as completed
Q - Quit"""
data_file = open("albums.csv", "r")
inform = [Album(line[0], line[1], int(line[2]), line[3]) for line in csv.reader(open("albums.csv"))]


def lists():
    """This function can list out the albums you have.
    You can know name,author,year and condition through it."""
    name = []
    author = []
    year = []
    condition = []
    inform.sort(key=attrgetter('year'))
    for index, album in enumerate(inform):
        if not album.is_completed:
            print(album.mark_required(), index+1, album.__str__().lstrip('*'))
        else:
            print(" ", index+1, album.__str__().lstrip(' '))
        name.append(album.title)
        author.append(album.artist)
        year.append(album.year)
        condition.append(album.is_completed)
    long = len(name)
    require = 0
    for i in range(1, long + 1, 1):
        if not inform[i - 1].is_completed:
            require = require + 1
    if "r" or 'False' in condition:
        print("You need to listen to {} albums".format(require))
    else:
        print("No albums left to listen to. Why not add a new album?")


def add():
    """This function help you to add new albums into the list.
    You should input title,artist and year of the new album."""

    def add_new():
        """This function can return the new album's information."""
        new = []
        title = input("Title:")
        while title != "" and title != " ":
            new.append(title)
            artist = input("Artist:")
            while artist != "" and artist != " ":
                new.append(artist)
                year = input("Year:")
                while year != "" and year != " ":
                    if year.isalpha() or isinstance(year, float):
                        print("Invalid input; enter a valid number")
                    elif year < "0" or year == "0":
                        print("Number must be > 0")
                    else:
                        new.append(year)
                        print("{} by {}({}) added to Album Tracker".format(new[0], new[1], new[2]))
                        # It's hard to break from these while loops without changing correct things
                        # so we can make a function to stop and return
                        return new
                    year = input("Year:")
                    print("Input can not be blank")
                artist = input("Artist:")
                print("Input can not be blank")
            print("Input can not be blank")
            title = input("Title:")

    new_album = add_new()
    new_album.append('False')
    inform.append(Album(new_album[0], new_album[1], new_album[2], new_album[3]))
    open("albums.csv", 'w').close()
    for album in inform:
        csv.writer(open('albums.csv', 'a', newline='')).writerow([album.title, album.artist, album.year,
                                                                 album.is_completed])


def mark():
    """This function can mark the albums from r to c.
    But you can not mark it from c to r."""
    condition = []
    for album in inform:
        condition.append(album.is_completed)
    if False not in condition:
        print("No required albums")
    else:
        lists()
        print("Enter the number of an album to mark as completed")
        m = input(">>>")
        while m.isalpha() or inform[int(float(m)) - 1].is_completed:
            # By this way,you can input letters ,int or float
            # All these can be right so can enter to judge
            if m.isalpha() or int(float(m)) != float(m):
                print("Invalid input; enter a valid number")
            elif m < "0" or m == "0":
                print("Number must be > 0")
            elif int(float(m)) > len(inform):
                print("Too large!The number must be under {}".format(len(inform)))
            else:
                print("You have already listened to ", inform[int(float(m)) - 1].title)
                break
            m = input(">>>")
        if not inform[int(m) - 1].is_completed:
            inform[int(m) - 1].is_completed = 'True'
            open("albums.csv", 'w').close()
            for album in inform:
                csv.writer(open('albums.csv', 'a', newline='')).writerow([album.title, album.artist, album.year,
                                                                         album.is_completed])
            print("You listened to {}".format(inform[int(m) - 1].title))


def main_menu():
    """This function can provide choices you can choose and jump to the function."""
    print("{} albums loaded".format(len(inform)))
    print(menu)
    choice = input(">>>").upper()
    while choice != "Q" and "4":
        if choice == "L" or choice == "1":
            lists()
        elif choice == "A" or choice == "2":
            add()
        elif choice == "M" or choice == "3":
            mark()
        else:
            print("Invalid menu choice")
        print(menu)
        choice = input(">>>").upper()
    print("{} albums saved to albums.csv".format(len(inform)))


def main():
    """This function mainly about how to execute."""
    print("Album Tracker 1.6 - by Yu hui Hua")
    main_menu()
    data_file.close()


main()
