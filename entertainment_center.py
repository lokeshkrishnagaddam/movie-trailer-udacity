import media
import fresh_tomatoes


def main():
    """ main function for creating the website """

    # create the instances of movies
  bahubali = media.Movies("BAHUBALI THE CONCLUSION",
                                "A story of a king",
                                "https://www.imdb.com/title/tt2631186/mediaviewer/rm4075110144.png",  # NOQA
                                "https://www.youtube.com/watch?v=G62HrubdD6o")  # NOQA

    mirchi = media.Movies("MIRCHI",
                                "About love",
                                "https://en.wikipedia.org/wiki/Mirchi_(film)#/media/File:Mirchi_Poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=I6QLMyeC1n8")  # NOQA

   temper = media.Movies("TEMPER",
                                "About a missing girl",
                                "http://3.bp.blogspot.com/-aBL2jjTCUeg/VLKbElMbFNI/AAAAAAAAAc4/OwE4Sebauig/s1600/Temper%2BMovie1.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=SQgRN5tu1f4")  # NOQA

   gowthamnanda = media.Movies("GOWTHAM NANDA",
                                        "About Money",
                                        "https://m.media-amazon.com/images/M/MV5BY2U1ZGQ2MGUtYzhhNC00NTg4LWEyODEtODY4YzNiNGUwMzNiXkEyXkFqcGdeQXVyMzYxOTQ3MDg@._V1_QL50_SY1000_CR0,0,705,1000_AL_.jpg",  # NOQA
                                        "https://www.youtube.com/watch?v=ztWcdGn5thU")  # NOQA

   bharatanenenu = media.Movies("BHARAT ANE NENU",
                            "About politics",
                            "https://en.wikipedia.org/wiki/Bharat_Ane_Nenu#/media/File:Bharat_Ane_Nenu_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=IvSoRWkaKn4&t=97s")  # NOQA

    srimanthudu = media.Movies("SRIMANTHUDU",
                            "The story of businessman",
                            "https://en.wikipedia.org/wiki/Srimanthudu#/media/File:Srimanthudu_poster.jpg",  # NOQA
                            "https://www.youtube.com/watch?v=dlvgG-hZ9xc")  # NOQA

    businessman = media.Movies("BUSINESSMAN",
                                    "About a man aiming for businessman",
                                    "http://www.manamahesh.com/BMDesigns/buesiness_man_60days_poster.jpg",  # NOQA
                                    "https://www.youtube.com/watch?v=xo_ZUn99wQ4")  # NOQA

    # create a list contains all the movies
    movies = [
        bahubali, mirchi, temper,
        gowthamnanda, bharatanenenu, srimanthudu,
        businessman
    ]

    # pass the list the fresh_tomatoes to create the website
    fresh_tomatoes.open_movies_page(movies)

if __name__ == '__main__':
    main()
