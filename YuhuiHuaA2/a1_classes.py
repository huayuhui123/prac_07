"""..."""
# Copy your first assignment to this file, then update it to use the Album class

from album import Album
import csv
from operator import itemgetter

menu = """Menu:
L - List all albums
A - Add new album
M - Mark an album as completed
Q - Quit"""
data_file = open("albums.csv", "r")
inform = [line for line in csv.reader(open("albums.csv"))]


def lists():
    """This function can list out the albums you have.
    You can know name,author,year and condition through it."""
    name = []
    author = []
    year = []
    condition = []
    for row in sorted(inform, key=itemgetter(1, 0)):
        # sort the list by author then by title
        # traverse all thing in list and append to gain classified information
        name.append(row[0])
        author.append(row[1])
        year.append(row[2])
        condition.append(row[3])
    long = len(name)
    require = 0
    for i in range(1, long + 1, 1):
        if condition[i - 1] == "r":
            print("*", end="")
            print("{}.{:<30} by {:<20}({})".format(i, name[i - 1], author[i - 1], year[i - 1]))
            require = require + 1
        else:
            print(" {}.{:<30} by {:<20}({})".format(i, name[i - 1], author[i - 1], year[i - 1]))
    if "r" in condition:
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
    new_album.append("r")
    inform.append(new_album)
    csv.writer(open('albums.csv', 'w', newline='')).writerow(inform)


def mark():
    """This function can mark the albums from r to c.
    But you can not mark it from c to r."""
    condition = []
    for row in inform:
        condition.append(row[3])
    if 'r' not in condition:
        print("No required albums")
    else:
        lists()
        print("Enter the number of an album to mark as completed")
        m = input(">>>")
        while m.isalpha() or inform[int(float(m)) - 1][3] != "r":
            # By this way,you can input letters ,int or float
            # All these can be right so can enter to judge
            if m.isalpha() or int(float(m)) != float(m):
                print("Invalid input; enter a valid number")
            elif m < "0" or m == "0":
                print("Number must be > 0")
            elif int(float(m)) > len(inform):
                print("Too large!The number must be under {}".format(len(inform)))
            else:
                print("You have already listened to ", (inform[int(float(m)) - 1][0]))
                break
            m = input(">>>")
        if inform[int(m) - 1][3] == 'r':
            inform[int(m) - 1][3] = 'c'
            csv.writer(open('albums.csv', 'w', newline='')).writerow(inform)
            print("You listened to{}".format(inform[int(m) - 1][0]))


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

