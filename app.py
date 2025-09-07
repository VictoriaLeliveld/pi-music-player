from flask import Flask, render_template
import os

app = Flask(__name__)
MUSIC_FOLDER = "static/music"

@app.route("/")
def index():
    songs = os.listdir(MUSIC_FOLDER)
    return render_template("index.html", songs=songs)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)