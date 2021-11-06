"""..."""


class Album:
    def __init__(self,title="",artist="",year=0,is_completed=False):
        self.title=title
        self.artist=artist
        self.year=year
        self.is_completed=is_completed

    def __str__(self):
        if not self.is_completed:
            print("*",end='')
        return "{:<30} by {:<20}({})".format(self.title, self.artist, self.year)

