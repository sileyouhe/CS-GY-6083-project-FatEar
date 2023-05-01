import datetime

from flask import Blueprint, request, render_template, session, redirect, url_for

from db import conn

song_bp = Blueprint('song_bp', __name__, template_folder='templates')


@song_bp.route('/search', methods=['GET', 'POST'])
def search():
    # grabs information from the forms
    # keyword = request.form['keyword']
    genre = request.form['genre']
    rating = request.form['rating']
    artist_first_name = request.form['artist_first_name']
    artist_last_name = request.form['artist_last_name']
    args = []
    print("  genre:" + genre + "  rating:" + rating + "  artfname:" + artist_first_name + " artlname" + artist_last_name)
    cursor = conn.cursor()
    sql = "SELECT * FROM song NATURAL JOIN songgenre LEFT OUTER JOIN song_avg_rating ON song.songID = song_avg_rating.songID LEFT OUTER JOIN (songinalbum NATURAL JOIN album) ON song.songID = songinalbum.songID LEFT OUTER JOIN (artist NATURAL JOIN artistperformssong) ON song.songID = artistperformssong.songID Where 1 = 1 "
    if genre and genre != "All":
        sql += ' and genre = %s'
        args.append(genre)
    if rating:
        sql += ' and avg_rating > %s'
        args.append(rating)
    if artist_first_name:
        sql += " and fname like CONCAT('%%', %s, '%%')"
        args.append(artist_first_name)
    if artist_last_name:
        sql += " and lname like CONCAT('%%', %s, '%%') "
        args.append(artist_last_name)
    cursor.execute(sql, args)

    result = cursor.fetchall()

    return render_template('song/song_result.html', result=result)

@song_bp.route('/searchGroup', methods=['GET', 'POST'])
def search_group():
    # grabs information from the forms
    # keyword = request.form['keyword']
    genre = request.form['genre']
    rating = request.form['rating']
    artist_first_name = request.form['artist_first_name']
    artist_last_name = request.form['artist_last_name']
    args = []
    print("  genre:" + genre + "  rating:" + rating + "  artfname:" + artist_first_name + " artlname" + artist_last_name)
    cursor = conn.cursor()
    sql = 'SELECT song.songID, song.title,GROUP_CONCAT(DISTINCT CONCAT(artist.fname, " ", artist.lname)) as artist, genre, avg_rating, GROUP_CONCAT(DISTINCT albumID) as albumID ' \
          'FROM song LEFT OUTER JOIN songgenre ON song.songID = songgenre.songID ' \
          'LEFT OUTER JOIN song_avg_rating ON song.songID = song_avg_rating.songID ' \
          'LEFT OUTER JOIN (songinalbum NATURAL JOIN album) ON song.songID = songinalbum.songID ' \
          'LEFT OUTER JOIN (artist NATURAL JOIN artistperformssong) ON song.songID = artistperformssong.songID ' \
          'Where 1 = 1 '

    if genre and genre != "All":
        sql += ' and genre = %s'
        args.append(genre)
    if rating:
        sql += ' and avg_rating > %s'
        args.append(rating)
    if artist_first_name:
        sql += " and fname like CONCAT('%%', %s, '%%')"
        args.append(artist_first_name)
    if artist_last_name:
        sql += " and lname like CONCAT('%%', %s, '%%') "
        args.append(artist_last_name)
    sql += "GROUP BY song.songID, song.title,genre,avg_rating"
    cursor.execute(sql, args)

    result = cursor.fetchall()
    print(result)
    return render_template('song/song_result.html', result=result)

@song_bp.route('/song/<songID>')
def get_song_detail(songID):
    sql_song_detail = "SELECT * FROM song NATURAL JOIN songgenre LEFT OUTER JOIN song_avg_rating ON song.songID = song_avg_rating.songID WHERE song.songID = %s "
    cursor = conn.cursor()
    cursor.execute(sql_song_detail, songID)
    song_detail = cursor.fetchone()

    sql_song_album = "SELECT GROUP_CONCAT(DISTINCT albumID) as albumID FROM song NATURAL JOIN songinalbum WHERE songID = %s "
    cursor.execute(sql_song_album, songID)
    song_album = cursor.fetchone()
    song_detail['album'] = song_album

    sql_song_artist = 'SELECT GROUP_CONCAT(CONCAT(artist.fname, " ", artist.lname)) as artist FROM artist NATURAL JOIN artistperformssong WHERE songID = %s '
    cursor.execute(sql_song_artist, songID)
    song_artist = cursor.fetchone()
    song_detail['artist'] = song_artist

    sql_review = "SELECT * FROM song NATURAL JOIN reviewsong WHERE song.songID = %s"
    cursor.execute(sql_review, songID)
    review = cursor.fetchall()
    song_detail['review'] = review
    user = session.get('user', None)
    if user:
        # if logged in, get the user's rating and review
        user_rating_sql = "SELECT * FROM ratesong WHERE username = %s AND songID = %s "
        cursor.execute(user_rating_sql, (user['username'], songID))
        user['rating'] = cursor.fetchone()
        user_review_sql = "SELECT * FROM reviewsong WHERE username = %s AND songID = %s "
        cursor.execute(user_review_sql, (user['username'],songID))
        user['review'] = cursor.fetchone()
    print(song_detail)
    print(user)
    return render_template('song/song_detail.html', song_detail=song_detail, user=user)

@song_bp.route("/rateSong", methods=['GET', 'POST'])
def rate_a_song():
    # grabs information from the forms
    username = request.form['username']
    rating = request.form['rating']
    songID = request.form['songID']

    cursor = conn.cursor()
    # check if this user has rated this song before
    query = "SELECT * from ratesong WHERE username = %s AND songID = %s"
    cursor.execute(query, (username, songID))
    data = cursor.fetchone()
    # if so, we update the latest rating and rating date
    if (data):
        now = datetime.date.today()
        updateStatement = 'UPDATE ratesong set stars = %s , ratingDate = %s WHERE username = %s AND songID = %s'
        cursor.execute(updateStatement, (rating, now, username, songID))
        conn.commit()
    else:
        # if not , we insert a new record into rating table
        now = datetime.date.today()
        insertStatement = 'INSERT INTO ratesong VALUES(%s, %s, %s, %s)'
        cursor.execute(insertStatement, (username, songID, rating, now))
        conn.commit()
    return redirect(url_for('song_bp.get_song_detail', songID=songID))


@song_bp.route("/postReview", methods=['GET', 'POST'])
def post_review():
    # grabs information from the forms
    username = request.form['username']
    reviewText = request.form['reviewText']
    songID = request.form['songID']

    cursor = conn.cursor()
    now = datetime.date.today()

    # check if this user has posted a review for this song before
    query = "SELECT * from reviewsong WHERE username = %s AND songID = %s"
    cursor.execute(query, (username, songID))
    data = cursor.fetchone()
    # if so, we update the latest review and review date
    if (data):
        updateStatement = 'UPDATE reviewsong set reviewText = %s , reviewDate = %s WHERE username = %s AND songID = %s'
        cursor.execute(updateStatement, (reviewText, now, username, songID))
        conn.commit()
    else:
        # if not , we insert a new record into review table
        insertStatement = 'INSERT INTO reviewsong VALUES(%s, %s, %s, %s)'
        cursor.execute(insertStatement, (username, songID, reviewText, now))
        conn.commit()

    return redirect(url_for('song_bp.get_song_detail', songID=songID))
