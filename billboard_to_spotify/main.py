from bs4 import BeautifulSoup
import requests as rq
import spotipy
from spotipy import SpotifyOAuth



# spotify 
CLIENT_ID = 'client ID from spotify account'
SECRET_ID = 'secret ID from spotify account'
REDIRECT_URI = 'http://example.com'
# INPUT
travel_date = input("What date would you like to travel to? Type date in the format YYYY-MM-DD: ")

# get website data
URL = f'https://www.billboard.com/charts/hot-100/{travel_date}/'
response = rq.get(url=URL)
soup = BeautifulSoup(response.text, 'html.parser')

# STRINGS OF CLASSES TO GET THE SONG TITLES
# the fist song uses a few different classes 
first_song_classes = 'c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021'
first_song_classes +=' u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max'
first_song_classes +=' a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet'
# the remaining 99 songs use the same classes
remaining_songs_classes = "c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021"
remaining_songs_classes += " lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125" 
remaining_songs_classes += " u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only"

# first song
first_song_title = soup.find(name="h3", id="title-of-a-story", class_= first_song_classes).getText().replace('\t','').replace('\n','')
song_titles = soup.find_all(name="h3", id="title-of-a-story", class_=remaining_songs_classes)

# save songs in a list  
song_list = []
song_list.append(first_song_title)
for tag in song_titles:
    song = tag.getText()
    song = song.replace('\t','').replace('\n','')
    song_list.append(song)


# CREATE AUTHENTICATION OBJECT
sp_obj = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=SECRET_ID,
    redirect_uri=REDIRECT_URI,
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path='token.txt'
))

# get the user information
information_obj = sp_obj.current_user()
user_id = information_obj['id']
# create a playlist
playlist = sp_obj.user_playlist_create(user=user_id,
    name=f"Biullboard Top100 on {travel_date}",
    public=False,
    collaborative=False,
    description=f"This playlist contains the top 100 songs of the Billboard chart on {travel_date}")


# each song has a URI which is used by spotify to find the song
uri_list = []
year = travel_date.split('-')[0]
for song in song_list:
    search_result = sp_obj.search(q=f'track:{song} year:{year}',type='track')
    try:
        uri = search_result["tracks"]["items"][0]["uri"]
        uri_list.append(uri)
    except IndexError:
        #print(f"{song} doesn't exist in Spotify. Skipped.")
        pass

# add the tracks to the playlist
sp_obj.playlist_add_items(playlist_id=playlist["id"], items=uri_list)