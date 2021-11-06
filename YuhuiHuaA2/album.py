"""..."""


class Album:
    def __init__(self,title="",artist="",year=0,is_completed=False):
        self.title=title
        self.artist=artist
        self.year=year
        self.is_completed=is_completed

    def mark_completed(self):
        if self.is_completed:
            pass

    def mark_required(self):
        if not self.is_completed:
            return "*"

    def __str__(self):
        if not self.is_completed:
            return "{}{:<30} by {:<20}({})".format(self.mark_required(),self.title, self.artist, self.year)
        else:
            return "{}{:<30} by {:<20}({})".format(self.mark_completed(),self.title, self.artist, self.year)


