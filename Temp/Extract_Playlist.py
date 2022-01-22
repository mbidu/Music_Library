# ctrl + K + C

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


#Authentication - without user
with open(r"C:\Users\mackt\Python\Music Libarary\Spotify_App_Credentials.txt") as f:
    sac_lines = f.readlines()
    cid = sac_lines[0].split(", ")
    cid = cid[1].split("\n")
    cid = cid[0]
    print(cid)
    secret = sac_lines[1].split(", ")
    secret = secret[1]
    print(secret)

client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

playlist_link = "https://open.spotify.com/playlist/7LaicnuGlBjUoHZ5Rd4tjm?si=e9f47ebd992b4d08"
# spotify:playlist:7LaicnuGlBjUoHZ5Rd4tjm
playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

for track in sp.playlist_tracks(playlist_URI)["items"]:
    #URI
    track_uri = track["track"]["uri"]

    #Track name
    track_name = track["track"]["name"]

    #Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)

    #Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]

    #Album
    album = track["track"]["album"]["name"]

    #Popularity of the track
    track_pop = track["track"]["popularity"]

    #Additional Features
    sp.audio_features(track_uri)[0]