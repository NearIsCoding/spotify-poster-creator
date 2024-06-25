import json
from requests import post, get

class SpotifySearchs:

    def __init__(self, token):
        self.token = token


    def get_auth_header(self):
        return {"Authorization": "Bearer " + self.token}

    def search_for_artist(self, artist_name):
        
        url = "https://api.spotify.com/v1/search"
        headers = self.get_auth_header()
        query = f"q={artist_name}&type=artist&limit=1"
        query_url = url + "?" + query
        
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)["artists"]["items"]
        
        if len(json_result) == 0:
            print("No artist found with that name")
            return None
        
        return json_result[0]
    
    def get_artist_id(self, artist):
        return artist["id"]
    
    def get_artist_albums(self, artist_id):
        url = f"https://api.spotify.com/v1/artists/{artist_id}/albums"
        headers = self.get_auth_header()
        query = "include_groups=album"
        query_url = url + "?" + query
        
        result = get(query_url, headers=headers)
        json_result = json.loads(result.content)["items"]
        
        return json_result

    def get_top_tracks_by_artist(self, artist_id):
        url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
        headers = self.get_auth_header()
        result = get(url, headers=headers)
        json_result = json.loads(result.content)["tracks"]
        return json_result