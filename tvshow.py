import webbrowser
from video import Video


class TVShow(Video):
    def __init__(self, title, storyline, poster, trailer):
        Video.__init__(self, title, storyline, poster, trailer)
