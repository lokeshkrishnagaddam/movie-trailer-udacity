import webbrowser


class Movie():
    def __init__(self, title, year, poster_url, trailer_url):
        """Args:
        title = a string of the movie's title
        year = an integer for the year of the movie's release
        poster_url = a string containing a URL to a poster image
        trailer_url = a string containing a youtube URL of the movie's trailer
        """
        self.title = title
        self.year = year
        self.poster_url = poster_url
        self.trailer_url = trailer_url
""" Opens trailer in a web browser """
