"""..."""


class Album:
    def __init__(self, title="", artist="", year=0, is_completed=False):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_completed = is_completed
        if self.is_completed == 'True' or self.is_completed == 'c':
            self.is_completed = True
        elif self.is_completed == 'False' or self.is_completed == 'r':
            self.is_completed = False

    def mark_completed(self):
        if self.is_completed or self.is_completed == 'c':
            return ' '

    def mark_required(self):
        if not self.is_completed or self.is_completed == 'r':
            return "*"

    def __str__(self):
        if not self.is_completed or self.is_completed == 'r':
            return "{}{:<30} by {:<20}({})".format(self.mark_required(), self.title, self.artist, self.year)
        elif self.is_completed or self.is_completed == 'c':
            return "{}{:<30} by {:<20}({})".format(self.mark_completed(), self.title, self.artist, self.year)
