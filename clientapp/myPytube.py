from pytube import YouTube

def getVideoData(url):
    yt = YouTube(url)

    variable_dict = {
        'thumbnail' : yt.thumbnail_url,
        'title' : yt.title,
        'desc' : yt.description,
        'duration' : yt.length,
        'progressiveStreams' : yt.streams.filter(progressive=True),
        'audioStreams' : yt.streams.filter(only_audio=True),
        'videoStreams' : yt.streams.filter(only_video=True),
        'views' : yt.views,
    }

    return variable_dict