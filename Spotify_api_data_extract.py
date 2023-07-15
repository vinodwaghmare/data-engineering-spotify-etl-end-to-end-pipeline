import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3                                                     # aws package to programmatically communicate with aws services 

def lambda_handler(event, context):
    client_id = os.environ.get('client_id')
    client_secret = os.environ.get('client_secret')
    from datetime import datetime
    
    client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlist_link = "https://open.spotify.com/playlist/37i9dQZEVXbNG2KDcFcKOF"
    playlist_URI = playlist_link.split("/")[-1]
    spotify_data = sp.playlist_tracks(playlist_URI)

    client = boto3.client('s3')
    
    file_name = 'spotify_raw_' + str(datetime.now()) + '.json'
    
    client.put_object(
        Bucket='spotify-etl-project-vinod',
        Key='raw_data/to_processed/' + file_name ,
        Body=json.dumps(spotify_data)
        )
    