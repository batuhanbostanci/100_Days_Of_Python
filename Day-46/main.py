import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint as pp


CLIENT_ID = "Yours"
CLIENT_SECRET = "Yours"

date_of_playlist = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
url = "https://www.billboard.com/charts/hot-100/"+date_of_playlist+"/"

response = requests.get(url=url)
song_information = response.text

soup = BeautifulSoup(song_information, "html.parser")
names_of_songs = soup.find_all(name="div", class_="o-chart-results-list-row-container")

name_list = []
for songs in names_of_songs:
    songs1 = songs.find(name="li", class_="lrv-u-width-100p")
    songs2 = songs1.find(name="li", class_="o-chart-results-list__item")
    song_name = songs2.find(name="h3", id="title-of-a-story").text.strip('\n')
    name_list.append(song_name)

# print(name_list)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

year = date_of_playlist.split("-")[0]

song_uris = []
for song in name_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"Song:{song} doesn't exist in Spotify")

playlist = sp.user_playlist_create(user=user_id, name=f"{date_of_playlist} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

