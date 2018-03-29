import webbrowser

# Parent class for movie and tv shows


class Video():
    def __init__(self, title, storyline, poster, trailer):
        self.title = title
        self.storyline = storyline
        self.poster = poster
        self.trailer = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer)
