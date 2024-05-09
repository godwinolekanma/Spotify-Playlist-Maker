import requests
from bs4 import BeautifulSoup
import os
from datetime import datetime
import spotipy
from spotipy.oauth2 import *

# Initialize variables
incorrect_input = True
billboard_url = ""
TIME_PERIOD = ""
year = ""

# Function to scrape Billboard data
def billboard_data(url):
    response = requests.get(url)
    billboard_website = response.text
    soup = BeautifulSoup(billboard_website, "html.parser")
    songArtist_titles = soup.find_all(name="li", class_="lrv-u-width-100p")
    songArtist_list = [song.getText().replace("\n", "").replace("\t", "") for song in songArtist_titles]
    top_100 = songArtist_list[:200:2]  # Assuming each song and artist are in consecutive elements
    return top_100

# Function to create Spotify playlist
def playlist_create(billboard):
    # Spotify authentication
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope="playlist-modify-private",
            redirect_uri="http://example.com",
            client_id=os.environ.get("SPOTIPY_CLIENT_ID"),
            client_secret=os.environ.get("SPOTIPY_CLIENT_SECRET"),
            show_dialog=True,
            cache_path="token.txt")
    )
    user_id = sp.current_user()["id"]
    # Create playlist
    playlist_id = sp.user_playlist_create(user=user_id,
                                          name=f"{TIME_PERIOD} Top 100",
                                          public=False,
                                          description=f"Top 100 songs of the year {TIME_PERIOD}")
    playlist_id = playlist_id["id"]
    # Get Billboard data and add tracks to the playlist
    tracks = billboard_data(billboard)
    track_list = []
    for track_item in tracks:
        uri = f"spotify:{track_item}:{year}"  # Assuming track_item contains track name and artist name
        try:
            track_list.append(sp.search(uri)["tracks"]["items"][0]["uri"])
        except IndexError:
            pass

    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_list, position=None)

# User input loop
while incorrect_input:
    TIME_PERIOD = input("which year do you want to travel to? type the date in the format YYYY-MM-DD: ")
    try:
        TIME_PERIOD = str(datetime.strptime(TIME_PERIOD, "%Y-%m-%d").date())
        year = str(datetime.strptime(TIME_PERIOD, "%Y-%m-%d").year)
    except ValueError:
        print("incorrect input")
    else:
        billboard_url = f"https://www.billboard.com/charts/hot-100/{TIME_PERIOD}/"
        incorrect_input = False

# Call playlist creation function
playlist_create(billboard_url)