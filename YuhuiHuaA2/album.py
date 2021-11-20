"""
Name:album
Date started:2021.11.6
Introduce:This class can include four methods,which can help you to instantiate
          albums and print clearly.
          Init,str,and two methods to mark the album as completed/required.
Github URL:https://github.com/huayuhui123/Assignment2.git
"""


class Album:
    def __init__(self, title="", artist="", year=0, is_completed=False):
        """Contains four attributes:title,artist,year,is_completed.
           Judge the condition of the list and chang them to make tests pass."""
        self.title = title
        self.artist = artist
        self.year = year
        self.is_completed = is_completed
        if self.is_completed == 'True' or self.is_completed == 'c':
            self.is_completed = True
        elif self.is_completed == 'False' or self.is_completed == 'r':
            self.is_completed = False
        # Judge parameters no matter c,r or True,False.

    def mark_completed(self):
        """If it is listened,just print a block."""
        if self.is_completed or self.is_completed == 'c':
            return ' '

    def mark_required(self):
        """If not listened yet,print a star to mark it."""
        if not self.is_completed or self.is_completed == 'r':
            return "*"

    def __str__(self):
        """Return a well formatted string."""
        if not self.is_completed or self.is_completed == 'r':
            return "{}{:<30} by {:<20}({})".format(self.mark_required(), self.title, self.artist, self.year)
        elif self.is_completed or self.is_completed == 'c':
            return "{}{:<30} by {:<20}({})".format(self.mark_completed(), self.title, self.artist, self.year)
