import datetime

from flask import Blueprint, request, render_template, session, redirect, url_for

from db import conn

artist_bp = Blueprint('artist_bp', __name__, template_folder='templates')

@artist_bp.route('/searchArtist', methods=['GET', 'POST'])
def search():
    # grabs information from the forms
    # keyword = request.form['keyword']
    artist_first_name = request.form['artist_first_name']
    artist_last_name = request.form['artist_last_name']
    args = []
    cursor = conn.cursor()
    sql = "SELECT * FROM artist WHERE 1=1"
    if artist_first_name:
        sql += " and fname like CONCAT('%%', %s, '%%')"
        args.append(artist_first_name)
    if artist_last_name:
        sql += " and lname like CONCAT('%%', %s, '%%') "
        args.append(artist_last_name)
    cursor.execute(sql, args)

    result = cursor.fetchall()

    return render_template('artist/artist_result.html', result=result)

@artist_bp.route('/artist/<artistID>')
def get_artist_detail(artistID):

    sql_artist_detail = "SELECT * FROM artist WHERE artistID = %s "
    cursor = conn.cursor()
    cursor.execute(sql_artist_detail, artistID)
    artist_detail = cursor.fetchone()

    sql_artist_perform = "SELECT * FROM artistperformssong NATURAL JOIN song WHERE artistID = %s "
    cursor.execute(sql_artist_perform, artistID)
    artist_perform = cursor.fetchall()
    artist_detail['perform'] = artist_perform
    user = session.get('user', None)
    if user:
        # if logged in, check if the user is the fan of this artist
        fan_sql = "SELECT * FROM userfanofartist WHERE username = %s and artistID = %s"
        cursor.execute(fan_sql, (user['username'], artistID))
        fan_status = cursor.fetchone()
        if fan_status:
            user['fan_status'] = True
        else:
            user['fan_status'] = False

    return render_template('artist/artist_detail.html', artist_detail=artist_detail, user=user)

@artist_bp.route("/fanRequest", methods=['GET', 'POST'])
def fan_request():
    sender = request.form['sender']
    artistID = request.form['artistID']
    cursor = conn.cursor()
    select_sql = "SELECT * FROM userfanofartist WHERE username = %s and artistID = %s "
    cursor.execute(select_sql, (sender, artistID))
    fan = cursor.fetchone()
    if not fan:
        insert_sql = "INSERT INTO userfanofartist VALUES(%s, %s)"
        cursor.execute(insert_sql, (sender, artistID))
        conn.commit()
    return redirect(url_for('artist_bp.get_artist_detail', artistID=artistID))


@artist_bp.route("/cancelFanRequest", methods=['GET', 'POST'])
def cancel_fan_request():
    sender = request.form['sender']
    artistID = request.form['artistID']
    cursor = conn.cursor()
    delete_sql = "DELETE FROM userfanofartist WHERE username = %s and artistID = %s"
    cursor.execute(delete_sql, (sender, artistID))
    conn.commit()
    return redirect(url_for('artist_bp.get_artist_detail', artistID=artistID))

