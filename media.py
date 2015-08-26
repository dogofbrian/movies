import webbrowser


class Movie():
    """Holds basic film information.

    Attributes:
        title : film title
        storyline : tag line or summary of the story
        poster_image_url : url to an image of the film poster
        trailer_youtube_url : link to the trailer on youtube
        duration : film duration in minutes
        rating: your rating of the film out of 5 (needs to be an integer)
    """

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url, duration, rating):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.duration = duration
        self.rating = rating

    def show_trailer(self):
        """Opens the film's trailer in youtube."""
        webbrowser.open_new(self.trailer_youtube_url)