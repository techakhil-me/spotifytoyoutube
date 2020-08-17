import re
from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, "index.html")


def getLink(request):
    link = False
    if request.method == "POST":
        link = request.POST.get('link')
        link = createLink(link)
    if link:
        return render(request, "index.html", {'link': link})
    else: 
        return render(request, "index.html",{'link': 'InvalidLink'})


def createLink(LINK):
    try:
        from spotipy.oauth2 import SpotifyClientCredentials
        import spotipy
        from youtube_search import YoutubeSearch


        client_credentials_manager = SpotifyClientCredentials(client_id='e5d66c188ef64dd89afa4d13f9555411',
                        client_secret='d070988d7bd5479a9e0818fa23839544')
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        PlaylistLink = "http://www.youtube.com/watch_videos?video_ids="
        for i in (sp.playlist_tracks(LINK)['items']):
            try:
                song = i['track']['name'] + i['track']['artists'][0]['name']
                PlaylistLink += (YoutubeSearch(song, max_results=1).to_dict()
                                )[0]['id'] + ','
            except:
                pass
        return PlaylistLink
    except:
        return False