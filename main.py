from Scripts.spotify_api_controller import SpotifyToken
from Scripts.spotify_searchs import SpotifySearchs
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

spotifyToken = SpotifyToken()
TOKEN = spotifyToken.get_token()
print('Token = ', TOKEN)
spotifySearchs = SpotifySearchs(TOKEN)

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        artistName = request.form['artistName']
        return redirect(url_for('album_selection', artistName=artistName))
    return render_template('search.html')


@app.route('/album_selection', methods=['POST', 'GET'])
def album_selection():
    artistName = request.args.get('artistName')
    artist = spotifySearchs.search_for_artist(artistName)
    if artist is None:
        return "No artist found with that name"
    
    artistId = spotifySearchs.get_artist_id(artist)
    albums = spotifySearchs.get_artist_albums(artistId)

    for i in range(len(albums)):
        print(albums[i]['name'])
    
    if request.method == 'POST':
        albumIndex = request.form['radio-card']
        albumIndex = int(albumIndex) - 1
        selectedAlbum = albums[albumIndex]
        selectedAlbumId = selectedAlbum['id']
        return redirect(url_for('album_info', selectedAlbumId=selectedAlbumId))

    return render_template('album_selection.html', artistName=artist['name'], albums=albums)

@app.route('/album_info', methods=['POST', 'GET'])
def album_info():
    selectedAlbumId = request.args.get('selectedAlbumId')
    return render_template('album_info.html', selectedAlbumId=selectedAlbumId)

if __name__ == '__main__':
    app.run(debug=True)