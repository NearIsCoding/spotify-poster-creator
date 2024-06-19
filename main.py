from spotify_api_controller import SpotifyToken
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

spotifyToken = SpotifyToken()
token = spotifyToken.get_token()
print(token)

@app.route('/', methods=['POST', 'GET'])
def home():
    return render_template('home.html')

@app.route('/search', methods=['POST', 'GET'])
def search():
    if request.method == 'POST':
        artistName = request.form['artistName']
        return redirect(url_for('show_info', artistName=artistName))
    return render_template('search.html')


@app.route('/show_info')
def show_info():
    artistName = request.args.get('artistName')
    return render_template('show_info.html', artistName=artistName)

if __name__ == '__main__':
    app.run(debug=True)