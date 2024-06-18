from spotify_api_controller import SpotifyToken
from flask import Flask, render_template

app = Flask(__name__)

spotifyToken = SpotifyToken()
token = spotifyToken.get_token()
print(token)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)