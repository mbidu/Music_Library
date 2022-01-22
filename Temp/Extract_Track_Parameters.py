import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re

def zed_to_features(zed):

    #Credentials
    with open(r"C:\Users\mackt\Python\Music Libarary\Spotify_App_Credentials.txt") as f:
        sac_lines = f.readlines()
        cid = sac_lines[0]
        cid = cid.split(",")
        cid = cid[1]
        secret = sac_lines[1]

    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)

    #Audio features
    features = sp.audio_features(zed)[0]

    #Artist of the track, for genres and popularity
    artist = sp.track(zed)["artists"][0]["id"]
    artist_pop = sp.artist(artist)["popularity"]
    artist_genres = sp.artist(artist)["genres"]

    #Track popularity
    track_pop = sp.track(zed)["popularity"]

    #Add in extra features
    features["artist_pop"] = artist_pop
    if artist_genres:
        features["genres"] = " ".join([re.sub(' ','_',i) for i in artist_genres])
    else:
        features["genres"] = "unknown"
    features["track_pop"] = track_pop

    print(cid) ###
    print(secret) ####
    return features

if __name__ == "__main__":
    # Debug
    result = zed_to_features("5MMZJtHOiH1RmQSSe3DJdg")
    print(result)
