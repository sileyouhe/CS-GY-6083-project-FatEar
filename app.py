from flask import Flask, render_template, session
from werkzeug.exceptions import HTTPException
import logging as logger
from user import user_bp
from song import song_bp
from artist import artist_bp
from db import conn
import config

app = Flask(__name__)
app.register_blueprint(user_bp)
app.register_blueprint(song_bp)
app.register_blueprint(artist_bp)
app.secret_key = config.SECRET_KEY

@app.route('/')
def hello():
    user = session.get('user', None)
    genres = get_genre()
    print("user = ", user)
    return render_template('index.html', genres=genres, user=user)



def get_genre():
    cursor = conn.cursor()
    query = 'SELECT distinct genre FROM songgenre'
    cursor.execute(query)
    genres = cursor.fetchall()
    cursor.close()
    return genres

@app.errorhandler(Exception)
def handle_exception(e):
    # pass through HTTP errors
    if isinstance(e, HTTPException):
        return e

    # now you're handling non-HTTP exceptions only
    return render_template("500_generic.html", e=e), 500

# if __name__ == '__main__':
#     app.debug = True
#     app.run()
