import fresh_tomatoes
import media



def __init__(self):
    b = media.M("BAHUBALI", "king", "https://en.wikipedia.org/wiki/Baahubali:_The_Beginning#/media/File:Baahubali_poster.jpg", "https://www.youtube.com/watch?v=qD-6d8Wo3do")  # NOQA
    m = media.M("MIRCHI", "About love", "https://en.wikipedia.org/wiki/Mirchi_(film)#/media/File:Mirchi_Poster.jpg", "https://www.youtube.com/watch?v=I6QLMyeC1n8")  # NOQA
    t = media.M("TEMPER", "About a missing girl", "http://3.bp.blogspot.com/-aBL2jjTCUeg/VLKbElMbFNI/AAAAAAAAAc4/OwE4Sebauig/s1600/Temper%2BMovie1.jpg", "https://www.youtube.com/watch?v=SQgRN5tu1f4")  # NOQA
    g = media.M("GOWTHAM NANDA", "About Money", "https://m.media-amazon.com/images/M/MV5BY2U1ZGQ2MGUtYzhhNC00NTg4LWEyODEtODY4YzNiNGUwMzNiXkEyXkFqcGdeQXVyMzYxOTQ3MDg@._V1_QL50_SY1000_CR0,0,705,1000_AL_.jpg", "https://www.youtube.com/watch?v=ztWcdGn5thU")  # NOQA
    b = media.M("BHARAT ANE NENU", "About politics", "https://en.wikipedia.org/wiki/Bharat_Ane_Nenu#/media/File:Bharat_Ane_Nenu_poster.jpg", "https://www.youtube.com/watch?v=IvSoRWkaKn4&t=97s")  # NOQA
    s = media.M("SRIMANTHUDU", "The story of businessman", "https://en.wikipedia.org/wiki/Srimanthudu#/media/File:Srimanthudu_poster.jpg", "https://www.youtube.com/watch?v=dlvgG-hZ9xc")  # NOQA
    bu = media.M("BUSINESSMAN", "About a man aiming for businessman", "http://www.manamahesh.com/BMDesigns/buesiness_man_60days_poster.jpg", "https://www.youtube.com/watch?v=xo_ZUn99wQ4")  # NOQA
    mo = [b, m, t, g, b, s, bu]
    fresh_tomatoes.open_movies_page(mo)

