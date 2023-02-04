# This is a baseline model to Automate a Spotify playlist with python
# Reference: https://www.youtube.com/watch?v=7J_qcttfnJA

# Step 1: Log Into Youtube
# Step 2: Grab Our Liked Videos
# Step 3: Create A New Playlist in Spotify
# Step 4: Search for the song
# Step 5: Add this song into the new Spotify playlist


# import the necessary packages

from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
import os
import json
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from spotipy.oauth2 import SpotifyClientCredentials




# create a class to automate the process


class CreatePlaylist:

    def __init__(self):
        """Create a new instance of the CreatePlaylist class"""
        self.user_id = "JackieSym" # add your user id
        self.youtube_client = self.get_youtube_client() # get the youtube client
        self.all_song_info = {} # create a dictionary to store the song info

    # Step 1: Log Into Youtube
    def get_youtube_client(self):
        """Log into Youtube and create a youtube client"""
        # Log into Youtube
        credentials = Credentials.from_authorized_user_info(info=None) # add your credentials
        youtube = build("youtube", "v3", credentials=credentials) # build the youtube client
        return youtube
        
    # Step 2: Grab Our Liked Videos and Create A Dictionary of Important Song Information
    def get_liked_videos(self):
        """Get a list of all liked videos"""
        request = self.youtube_client.videos().list( # get the list of liked videos
            part="snippet,contentDetails,statistics", # get the snippet, content details and statistics
            myRating="like" # get the liked videos
        )
        response = request.execute() # execute the request

        for item in response ["items"]: # loop through the items
            video_title = item["snippet"]["title"] # get the title of the video
            video_id = item["id"] # get the id of the video
            self.all_song_ingo[video_title] = video_id # add the video title and id to the dictionary

    # Step 3: Create A New Playlist in Spotify
    def create_playlist(self):
        """Create a new playlist"""
        request = self.youtube_client.playlists().insert(
            part="snippet,status",  # get the snippet and status
            body={
                "snippet": {
                    "title": "Liked Videos",
                    "description": "A playlist of all liked videos", 
                    "tags": [
                        "liked videos",
                        "youtube",
                        "music"
                    ],
                    "defaultLanguage": "en"
                },
                "status": {
                    "privacyStatus": "private"
                }
            }
        )
        response = request.execute() # execute the request
        return response["id"] # return the playlist id
    
    # Step 4: get the spotify token

    def get_spotify_token(self):
        # Load the Spotify API credentials from environment variables.
        client_id = os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
        credentials = SpotifyClientCredentials(client_id, client_secret)
        return credentials.get_access_token()
        

    # Step 5: Search for the song
    def get_spotify_uri(self, song_name, artist): # add the song name and artist
        query = f"{song_name} {artist}" # create the query
        result = self.spotify_client.search(q = query, type = "track") # search for the song
        tracks = result["tracks"]["items"] # get the tracks
        if len(tracks) > 0: # if there are tracks
            return tracks[0]["uri"] # return the uri of the first track
        else:
            return None

    # Step 6: Add this song into the new Spotify playlist
    def add_song_to_playlist(self):
        for song, video_id in self.all_song_info.items():
            song_name, artist = self.get_song_and_artist_from_video_title(song)
            spotify_uri = self.get_spotify_uri(song_name, artist)
            if spotify_uri is not None:
                request_body = json.dumps([spotify_uri])
                self.spot
        

if __name__ == '__main__':
    cp = CreatePlaylist()
    cp.get_liked_videos()

