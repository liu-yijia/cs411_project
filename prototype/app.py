#tutorial: https://github.com/himanshukamal/spotify-music/blob/main/app.py

from flask import Flask, render_template, redirect, url_for, request,jsonify
app = Flask(__name__)

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
	client_id
	client_secret
	)
)

@app.route('/',methods = ['POST', 'GET'])
def login():
	if request.method == 'POST':
		search_text = request.form['nm']

		results = sp.search(q=search_text, limit=10)
		# for idx, track in enumerate(results['tracks']['items']):
		# 	print(idx, track['name'])
		songlist = results['tracks']['items']

		return render_template('spotify-search.html', tracks=songlist)
		# return jsonify(results)
	else:
		user = request.args.get('nm')
		return render_template('spotify-search.html')

if __name__ == '__main__':
	app.run(debug = True)
