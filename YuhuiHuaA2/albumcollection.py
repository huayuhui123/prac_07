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
        self.albums = [Album(line) for line in csv.reader(open(filename))]
        data_file.close()

    def sort(self):
        self.albums.sort(key=attrgetter('title', 'year'))
        print(self.albums)

    def add_album(self):
        pass

