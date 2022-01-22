#!/usr/bin/env python
# coding: utf-8

# In[29]:


# jupyter nbconvert --to python Extract_Playlist_With_Duplicates.ipynb

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import csv
import pandas as pd


# In[ ]:


print("...Making CSV...")


# In[30]:


#Authentication - without user
with open(r"C:\Users\mackt\Python\Music Library\Spotify_App_Credentials.txt") as f:
    sac_lines = f.readlines()
    cid = sac_lines[0].split(", ")
    cid = cid[1].split("\n")
    cid = cid[0]
    # print(cid)
    secret = sac_lines[1].split(", ")
    secret = secret[1]
    # print(secret)


# In[31]:


client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials_manager)


# In[32]:


playlist_link = "https://open.spotify.com/playlist/7LaicnuGlBjUoHZ5Rd4tjm?si=e9f47ebd992b4d08"
playlist_URI = playlist_link.split("/")[-1].split("?")[0]


# In[33]:



# for track in sp.playlist_tracks(playlist_URI)["items"]:
#     artist_uri = track["track"]["artists"][0]["uri"]
#     artist_info = sp.artist(artist_uri)
# print(artist_info)


# In[34]:


# print(sp.playlist_tracks(playlist_URI))


# In[35]:


# for track in sp.playlist_tracks(playlist_URI)["items"]:
#     track_uri = track["track"]["uri"]

# print(sp.track(track_uri))


# In[36]:


# for track in sp.playlist_tracks(playlist_URI)["items"]:
#     track_uri = track["track"]["uri"]

# print(sp.audio_features(track_uri)[0])


# In[37]:


# Song Library
track_id = 1

sl_tr_id = []
sl_tr_uri = []
sl_tr_name = []

sl_ar_uri = []
sl_ar_names =[]
sl_ar_name = []
sl_ar_name2 = []
sl_ar_name3 = []
sl_ar_name4 = []
sl_ar_name5 = []
sl_ar_name6 = []
sl_ar_name7 = []
sl_ar_name8 = []
sl_ar_name9 = []
sl_ar_name10 = []

sl_tr_duration_ms =[]
sl_tr_album = []
sl_tr_pop = []

sl_tr_danceability = []
sl_tr_energy = []
sl_tr_key = []
sl_tr_loudness = []
sl_tr_mode = []
sl_tr_speechiness = []
sl_tr_acousticness = []
sl_tr_instrumentalness = []
sl_tr_liveness = []
sl_tr_valence = []
sl_tr_tempo = []

Duplicate_Index = []
Duplicate_ID = []


# In[38]:


for track in sp.playlist_tracks(playlist_URI)["items"]:
    # Track Name and URI
    track_name = track["track"]["name"]
    track_uri = track["track"]["uri"]
    sl_tr_uri.append(track_uri)

    # Artists
    track_artists_name = []
    track_artists_uri = []

    i = 0
    for i in range (10):
        artist_uri = track["track"]["artists"][i]["uri"]

        track_artists_uri.append(track["track"]["artists"][i]["uri"])
        track_artists_name.append(track["track"]["artists"][i]["name"])

        i = i + 1
        try: track["track"]["artists"][i]["name"]
        except IndexError:
            for y in range (10-i):
                track_artists_uri.append("")
                track_artists_name.append("")
            break

    # Add Artists To Song Library
    sl_ar_uri.append(track_artists_uri)

    sl_ar_names.append(track_artists_name)

    sl_ar_name.append(track_artists_name[0])
    sl_ar_name2.append(track_artists_name[1])
    sl_ar_name3.append(track_artists_name[2])
    sl_ar_name4.append(track_artists_name[3])
    sl_ar_name5.append(track_artists_name[4])
    sl_ar_name6.append(track_artists_name[5])
    sl_ar_name7.append(track_artists_name[6])
    sl_ar_name8.append(track_artists_name[7])
    sl_ar_name9.append(track_artists_name[8])
    sl_ar_name10.append(track_artists_name[9])

    # Track Duration
    track_duration_ms = sp.audio_features(track_uri)[0]["duration_ms"]
    sl_tr_duration_ms.append(track_duration_ms)

    # Track Album
    album = track["track"]["album"]["name"]
    sl_tr_album.append(album)

    # Track Popularity
    track_pop = track["track"]["popularity"]
    sl_tr_pop.append(track_pop)

    # Track Audio Features
    sl_tr_danceability.append(sp.audio_features(track_uri)[0]["danceability"])
    sl_tr_energy.append(sp.audio_features(track_uri)[0]["energy"])
    sl_tr_key.append(sp.audio_features(track_uri)[0]["key"])
    sl_tr_loudness.append(sp.audio_features(track_uri)[0]["loudness"])
    sl_tr_mode.append(sp.audio_features(track_uri)[0]["mode"])
    sl_tr_speechiness.append(sp.audio_features(track_uri)[0]["speechiness"])
    sl_tr_acousticness.append(sp.audio_features(track_uri)[0]["acousticness"])
    sl_tr_instrumentalness.append(sp.audio_features(track_uri)[0]["instrumentalness"])
    sl_tr_liveness.append(sp.audio_features(track_uri)[0]["liveness"])
    sl_tr_valence.append(sp.audio_features(track_uri)[0]["valence"])
    sl_tr_tempo.append(sp.audio_features(track_uri)[0]["tempo"])

    # Duplicate Songs
    current_index = len(sl_tr_name)
    if track_name in sl_tr_name:
        dup_index = sl_tr_name.index(track_name)
        if sl_ar_uri[dup_index] == track_artists_uri:
            Duplicate_Index[dup_index] = dup_index
            Duplicate_Index.append(dup_index)
    else:
        Duplicate_Index.append('')

    # Add Track Name Now
    # Avoids disturbing Duplicates
    sl_tr_name.append(track_name)


# In[39]:


# print(sp.audio_features(track_uri)[0])


# In[40]:


# Song Library
df = pd.DataFrame()

df['ID'] = ''
df['Duplicates'] = Duplicate_Index
df['Song'] = sl_tr_name
df['Artist 1'] = sl_ar_name
df['Artist 2'] = sl_ar_name2
df['Artist 3'] = sl_ar_name3
df['Artist 4'] = sl_ar_name4
df['Artist 5'] = sl_ar_name5
df['Artist 6'] = sl_ar_name6
df['Artist 7'] = sl_ar_name7
df['Artist 8'] = sl_ar_name8
df['Artist 9'] = sl_ar_name9
df['Artist 10'] = sl_ar_name10
df['Duration'] = sl_tr_duration_ms
df['Album'] = sl_tr_album
df['Popularity'] = sl_tr_pop

df['Dance'] = sl_tr_danceability
df['Energy'] = sl_tr_energy
df['Key'] = sl_tr_key
df['Volume'] = sl_tr_loudness
df['Mode'] = sl_tr_mode
df['Speech'] = sl_tr_speechiness
df['Acoustic'] = sl_tr_acousticness
df['Instrumental'] = sl_tr_instrumentalness
df['Lively'] = sl_tr_liveness
df['Valence'] = sl_tr_valence
df['Tempo'] = sl_tr_tempo

df['URI'] = sl_tr_uri
df['Artists URIs'] = sl_ar_uri

# Sort Alphabetically by Artist -> Album -> Song
df = df.sort_values(['Artist 1', 'Album', 'Song'], ascending = True, key = lambda col: col.str.lower())

# Track IDs
sl_tr_id = list(range(1,len(sl_tr_name)+1))
df['ID'] = sl_tr_id

#Creating CSV
df.to_csv(r'C:\Users\mackt\Python\Music Library\Data\Music_Gala_With_Duplicates.csv',index = False)


# In[41]:


# # Duplicate Track Highlighting
# Duplicate_Tracks = pd.read_csv(r'C:\Users\mackt\Python\Music Library\Data\Music_Gala_With_Duplicates.csv', names = ['Duplicates'])

# def Duplicate_Tracks(row):
#     if row['Duplicates'] != '':
#         return ['background-color: red'] * len(row)
#     else:
#         return ['background-color: green'] * len(row)

# df.style.apply(Duplicate_Tracks, axis = 1)


# In[42]:


# print(df)

