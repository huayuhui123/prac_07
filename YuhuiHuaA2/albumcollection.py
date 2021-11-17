"""..."""

import csv
from operator import attrgetter
from album import Album


class AlbumCollection:
    def __init__(self, albums=None):
        self.albums = albums

    def __str__(self):
        return str(self.albums)

    def load_albums(self, filename=None):
        data_file = open(filename, "r")
        self.albums = [Album(line[0], line[1], int(line[2]), line[3]) for line in csv.reader(open(filename))]
        data_file.close()

    def sort(self):
        self.albums.sort(key=attrgetter('year'))

    def add_album(self, new_album=None):
        self.albums.append(new_album)

    def save_albums(self):
        open("albums.csv", 'w').close()
        for album in self.albums:
            csv.writer(open('albums.csv', 'a', newline='')).writerow([album.title, album.artist, album.year,
                                                                      album.is_completed])
