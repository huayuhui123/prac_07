"""
Name:albumcollection
Date started:2021.11.7
Introduce:This class include 6 important functions-init,str,load,sort and add albums.
          They are combined firmly with csv file so they can change the file directly.
Github URL:https://github.com/huayuhui123/Assignment2.git
"""

import csv
from operator import attrgetter
from album import Album


class AlbumCollection:
    def __init__(self, albums=None):
        """Get the list of albums and initialize them.
           The new attribute of this class is just a list."""
        self.albums = albums

    def __str__(self):
        """Return the list consists of all albums' addresses."""
        return str(self.albums)

    def load_albums(self, filename=None):
        """Get the file's name,open and read to store them in a list."""
        data_file = open(filename, "r")
        self.albums = [Album(line[0], line[1], int(line[2]), line[3]) for line in csv.reader(open(filename))]
        # These information read from csv should be a list,but we should divide them,or all things will be in title
        # artist,year and condition will be empty.
        data_file.close()

    def sort(self):
        """Sort them by the key passed in, then by year"""
        self.albums.sort(key=attrgetter('year'))

    def add_album(self, new_album=None):
        """Add a single Album object to the albums attribute"""
        self.albums.append(new_album)

    def save_albums(self):
        """From album list into csv file.Clean and rewrite these information is very brief."""
        open("albums.csv", 'w').close()
        for album in self.albums:
            csv.writer(open('albums.csv', 'a', newline='')).writerow([album.title, album.artist, album.year,
                                                                      album.is_completed])
