import requests
import bs4
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_id = "your client id"
client_secret = "your client secret"

#step1
date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD:")
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
url = "https://www.billboard.com/charts/hot-100/" + date
response = requests.get(url, headers=header)

soup = bs4.BeautifulSoup(response.text, "html.parser")
songs = soup.select("li ul li h3")
song_names = [song.getText().split() for song in songs]

#step2
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id=client_id,
        client_secret=client_secret,
        show_dialog=True,
        cache_path="token.txt",
        username="your username"
    ))
user_id = sp.current_user()["id"]

#step3
song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song},year:{year}", type="track")
    try:
        song_id = result["tracks"]["items"][0]["id"]
        song_uris.append(song_id)
    except IndexError:
        print(f"{song} does not exist in Spotify. Skipped.")

#step4
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{date} Billboard 100",
    public=False,
    description="Spotify Playlist"
)
sp.playlist_add_items(
    playlist_id=playlist["id"],
    items=song_uris
)
