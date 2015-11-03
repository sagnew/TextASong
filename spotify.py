import requests


def get_track_url(song_title):
    spotify_url = 'https://api.spotify.com/v1/search'
    params = {'q': song_title, 'type': 'track'}

    spotify_response = requests.get(spotify_url, params=params).json()
    track_url = spotify_response['tracks']['items'][0]['preview_url']
    return track_url
