"""..."""

import csv


class AlbumCollection:
    def __init__(self, albums=None):
        self.albums = albums

    def __str__(self):
        return str(self.albums)

    def load_albums(self, filename=None):
        data_file = open(filename, "r")
        self.albums = [line for line in csv.reader(open(filename))]
        data_file.close()

    def sort(self):
        pass

    def add_album(self):
        pass

