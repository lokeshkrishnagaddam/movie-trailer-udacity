class Movies:
    """ class for storing movie info """
    def __init__(self, movie_titles, movie_storylines, poster_images,trailers_youtube):
        self.titles = movie_titles
        self.storylines = movie_storylines
        self.poster_image_urls = poster_images
        self.trailer_youtube_urls = trailers_youtube
