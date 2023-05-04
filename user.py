# Import Flask Library
import datetime
import bcrypt
from flask import render_template, request, session, url_for, redirect, flash, Blueprint
# from app import app
from db import conn

user_bp = Blueprint('user_bp', __name__, template_folder='templates')


# Define route for login
@user_bp.route('/login')
def login():
    return render_template('login.html')


# Define route for register
@user_bp.route('/register')
def register():
    return render_template('register.html')


# Authenticates the login
@user_bp.route('/loginAuth', methods=['GET', 'POST'])
def loginAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM user WHERE username = %s'
    cursor.execute(query, username)
    # stores the results in a variable
    user = cursor.fetchone()
    print(user)
    # use fetchall() if you are expecting more than 1 data row
    error = None
    if (user):
        print(user)
        PasswordBytes = password.encode('utf-8')
        hashedPassword = user['pwd'].encode('utf-8')
        matches = bcrypt.checkpw(PasswordBytes, hashedPassword)
        if matches:
            # creates a session for the user
            # session is a built-in
            # update the lastlogin date
            now = datetime.date.today()
            updateStatement = 'UPDATE user set lastlogin = %s where username=%s'
            cursor.execute(updateStatement, (now, username))
            conn.commit()

            # Do not return the password of the user
            user['pwd'] = None
            # session['username'] = username
            session['user'] = user
            print(user)
            if user['lastlogin']:
                user['lastlogin'] = user['lastlogin'].strftime('%Y-%m-%d')
            return redirect(url_for('user_bp.home'))
        else:
            # returns an error message to the html page
            error = 'Invalid username or password'
            return render_template('login.html', error=error)
    else:
        # returns an error message to the html page
        error = 'Invalid username or password'
        return render_template('login.html', error=error)


# Authenticates the register
@user_bp.route('/registerAuth', methods=['GET', 'POST'])
def registerAuth():
    # grabs information from the forms
    username = request.form['username']
    password = request.form['password']
    fname = request.form['fname']
    lname = request.form['lname']
    nickname = request.form['nickname']

    # cursor used to send queries
    cursor = conn.cursor()
    # executes query
    query = 'SELECT * FROM user WHERE username = %s'
    cursor.execute(query, username)
    # stores the results in a variable
    data = cursor.fetchone()
    # use fetchall() if you are expecting more than 1 data row
    error = None
    if (data):
        # If the previous query returns data, then user exists
        error = "This user already exists"
        return render_template('register.html', error=error)
    else:
        # converting password to array of bytes
        passwordBytes = password.encode('utf-8')

        # generating the salt and then Hashing the password
        hashedPassword = bcrypt.hashpw(passwordBytes, bcrypt.gensalt())

        ins = 'INSERT INTO user VALUES(%s, %s, %s, %s, null, %s)'
        cursor.execute(ins, (username, hashedPassword, fname, lname, nickname))
        conn.commit()
        cursor.close()
        return render_template('index.html')


@user_bp.route('/home')
def home():
    return redirect(url_for('hello'))


@user_bp.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')


@user_bp.route('/searchUser', methods=['GET', 'POST'])
def search():
    # grabs information from the forms
    username = request.form['username']
    user_first_name = request.form['user_first_name']
    user_last_name = request.form['user_last_name']
    args = []
    print("  username:" + username + "  fname:" + user_first_name + "  lname:" + user_last_name)
    cursor = conn.cursor()
    sql = "SELECT username, fname, lname, nickname FROM user WHERE 1=1"
    if username:
        sql += " and username like CONCAT('%%', %s, '%%')"
        args.append(username)
    if user_first_name:
        sql += " and fname like CONCAT('%%', %s, '%%')"
        args.append(user_first_name)
    if user_last_name:
        sql += " and lname like CONCAT('%%', %s, '%%')"
        args.append(user_last_name)
    cursor.execute(sql, args)

    result = cursor.fetchall()

    return render_template('user/user_result.html', result=result)


@user_bp.route('/user/<username>')
def get_user_detail(username):
    sql_user_detail = "SELECT username, fname, lname, nickname FROM user WHERE username = %s "
    cursor = conn.cursor()
    cursor.execute(sql_user_detail, username)
    user_detail = cursor.fetchone()

    user = session.get('user', None)
    if user and user['username'] != username:
        # if logged in, check friend status
        friend_sql = "SELECT * FROM friend WHERE user1 = %s AND user2 = %s "
        cursor.execute(friend_sql, (username, user['username']))
        friend_status_1 = cursor.fetchone()
        cursor.execute(friend_sql, (user['username'], username))
        friend_status_2 = cursor.fetchone()
        user['friend_status'] = False
        if friend_status_1:
            if friend_status_1['acceptStatus'] == "Accepted":
                user['friend_status'] = True
        if friend_status_2:
            if friend_status_2['acceptStatus'] == "Accepted":
                user['friend_status'] = True

        # if logged in, check follow status
        follower_sql = "SELECT * FROM follows WHERE follower = %s and follows = %s "
        cursor.execute(follower_sql, (username, user['username']))
        follower_status = cursor.fetchone()
        if follower_status:
            user['follower_status'] = True
        else:
            user['follower_status'] = False

        follows_sql = "SELECT * FROM follows WHERE follower = %s and follows = %s "
        cursor.execute(follows_sql, (user['username'], username))
        follows_status = cursor.fetchone()
        if follows_status:
            user['follows_status'] = True
        else:
            user['follows_status'] = False

    info = request.args.get('info')
    return render_template('user/user_detail.html', user_detail=user_detail, user=user, info=info)


@user_bp.route("/friendRequest", methods=['GET', 'POST'])
def friend_request():
    sender = request.form['sender']
    receiver = request.form['receiver']
    cursor = conn.cursor()
    friend_sql = "SELECT * FROM friend WHERE requestSentBy = %s AND (user1 = %s OR user2 = %s) "
    cursor.execute(friend_sql, (sender, receiver, receiver))
    friend_status = cursor.fetchone()

    now = datetime.datetime.now()
    request_info = None
    # check if there is a record in the friend table
    if friend_status:
        # if so, we update the status and update timestamp
        update_sql = "UPDATE friend SET acceptStatus = 'Pending', updatedAt = %s WHERE requestSentBy = %s AND (user1 = %s OR user2 = %s) "
        cursor.execute(update_sql, (now, sender, receiver, receiver))
        conn.commit()
        request_info = "Your friend request has been updated at " + now.strftime("%Y-%m-%d %H:%M:%S")
    else:
        # if not, we insert a new record into the friend table
        insert_sql = "INSERT INTO friend VALUES(%s, %s, %s, %s, %s, %s)"
        cursor.execute(insert_sql, (sender, receiver, "Pending", sender, now, now))
        conn.commit()
        request_info = "Your friend request has been created at " + now.strftime("%Y-%m-%d %H:%M:%S")
    print(request_info)
    return redirect(url_for('user_bp.get_user_detail', username=receiver, info=request_info))


@user_bp.route("/myFriend/<username>", methods=['GET', 'POST'])
def get_friend(username):
    cursor = conn.cursor()
    result = {}
    # get all friends of the user
    friend_sql = "SELECT user2 as user FROM friend WHERE user1 = %s AND acceptStatus = 'accepted' UNION SELECT user1 as user FROM friend WHERE user2 = %s AND acceptStatus = 'accepted'"
    cursor.execute(friend_sql, (username, username))
    friends = cursor.fetchall()

    # get all friend requests of this user has sent
    request_send_sql = "SELECT * FROM friend  WHERE requestSentBy = %s ORDER BY friend.updatedAt DESC"
    cursor.execute(request_send_sql, username)
    request_send = cursor.fetchall()

    # get all friend requests of this user has received
    request_receive_sql = "SELECT * FROM friend WHERE (user1 = %s OR user2 = %s) AND requestSentBy != %s ORDER BY friend.updatedAt DESC "
    cursor.execute(request_receive_sql, (username, username, username))
    request_receive = cursor.fetchall()

    result['friends'] = friends
    result['request_send'] = request_send
    result['request_receive'] = request_receive
    return render_template('user/my_friend.html', result=result)


@user_bp.route("/acceptFriend/<sender>/<receiver>", methods=['GET', 'POST'])
def accept_request(sender, receiver):
    cursor = conn.cursor()
    now = datetime.datetime.now()
    update_sql = "UPDATE friend SET acceptStatus = 'Accepted', updatedAt = %s WHERE requestSentBy = %s AND (user1 = %s OR user2 = %s) "
    cursor.execute(update_sql, (now, sender, receiver, receiver))
    conn.commit()
    return redirect(url_for('user_bp.get_friend', username=receiver))


@user_bp.route("/rejectFriend/<sender>/<receiver>", methods=['GET', 'POST'])
def reject_request(sender, receiver):
    cursor = conn.cursor()
    now = datetime.datetime.now()
    update_sql = "UPDATE friend SET acceptStatus = 'Not accepted', updatedAt = %s WHERE requestSentBy = %s AND (user1 = %s OR user2 = %s) "
    cursor.execute(update_sql, (now, sender, receiver, receiver))
    conn.commit()
    return redirect(url_for('user_bp.get_friend', username=receiver))


@user_bp.route("/followRequest", methods=['GET', 'POST'])
def follow_request():
    sender = request.form['sender']
    receiver = request.form['receiver']
    cursor = conn.cursor()
    select_sql = "SELECT * FROM follows WHERE follower = %s and follows = %s "
    cursor.execute(select_sql, (sender, receiver))
    follow = cursor.fetchone()
    now = datetime.datetime.now()
    if not follow:
        insert_sql = "INSERT INTO follows VALUES(%s, %s, %s)"
        cursor.execute(insert_sql, (sender, receiver, now))
        conn.commit()
    request_info = "Follow this user successfully "
    return redirect(url_for('user_bp.get_user_detail', username=receiver, info = request_info))


@user_bp.route("/unfollowRequest", methods=['GET', 'POST'])
def unfollow_request():
    sender = request.form['sender']
    receiver = request.form['receiver']
    cursor = conn.cursor()
    delete_sql = "DELETE FROM follows WHERE follower = %s and follows = %s"
    cursor.execute(delete_sql, (sender, receiver))
    conn.commit()
    request_info = "Unfollow this user successfully "
    return redirect(url_for('user_bp.get_user_detail', username=receiver, info=request_info))


@user_bp.route("/myFollow/<username>", methods=['GET', 'POST'])
def get_follow(username):
    cursor = conn.cursor()
    result = {}
    # get all followers of the user
    follower_sql = "SELECT follower,fname,lname FROM follows JOIN user ON follows.follower = user.username WHERE follows = %s "
    cursor.execute(follower_sql, username)
    follower = cursor.fetchall()

    # get all other users that the user are following
    follows_sql = "SELECT follows,fname,lname FROM follows JOIN user ON follows.follows = user.username WHERE follower = %s "
    cursor.execute(follows_sql, username)
    follows = cursor.fetchall()

    result['follower'] = follower
    result['follows'] = follows
    print(result)
    return render_template('user/my_follow.html', result=result)

@user_bp.route("/myArtist/<username>", methods=['GET', 'POST'])
def get_artist(username):
    cursor = conn.cursor()
    result = {}
    # get all artists that the user follows
    artist_sql = "SELECT * FROM artist NATURAL JOIN userfanofartist WHERE username = %s"
    cursor.execute(artist_sql, username)
    artist = cursor.fetchall()
    result['artist'] = artist

    return render_template('user/my_artist.html', result=result)

@user_bp.route("/myRatingsAndReviews/<username>", methods=['GET', 'POST'])
def get_rating_and_review(username):
    cursor = conn.cursor()
    result = {}

    # get all the ratings
    ratings_sql = "SELECT * FROM ratesong NATURAL JOIN song WHERE username = %s "
    cursor.execute(ratings_sql, username)
    ratings = cursor.fetchall()
    result['ratings'] = ratings

    # get all the reviews
    reviews_sql = "SELECT * FROM reviewsong NATURAL JOIN song WHERE username = %s"
    cursor.execute(reviews_sql, username)
    reviews = cursor.fetchall()
    result['reviews'] = reviews
    print(result)
    return render_template('user/my_rating_and_review.html', result=result)

@user_bp.route("/myNewItems/<username>/<lastlogin>", methods=['GET', 'POST'])
def get_new_item(username, lastlogin):
    result = {}
    if lastlogin == "None":
        lastlogin = None
    new_reviews = get_new_reviews(username, lastlogin)
    new_songs = get_new_songs(username, lastlogin)
    result['new_reviews'] = new_reviews
    result['new_songs'] = new_songs
    print(result)
    return render_template('user/new_items.html', result=result, lastlogin= lastlogin)


def get_new_reviews(username, lastlogin):
    result = {}
    cursor = conn.cursor()
    # review song
    query = 'SELECT * FROM reviewsong NATURAL JOIN song WHERE reviewDate > %s AND username in ' \
            '(SELECT follows as user from follows WHERE follower = %s' \
            ' UNION SELECT user2 as user FROM friend WHERE user1 = %s and acceptStatus = "accepted" ' \
            ' UNION SELECT user1 as user FROM friend WHERE user2 = %s and acceptStatus = "accepted")'
    cursor.execute(query, (lastlogin, username, username, username))
    review_song = cursor.fetchall()
    result['review_song'] = review_song
    # review album
    query = 'SELECT * FROM reviewalbum WHERE reviewDate > %s AND username in ' \
            '(SELECT follows as user from follows WHERE follower = %s' \
            ' UNION SELECT user2 as user FROM friend WHERE user1 = %s and acceptStatus = "accepted" ' \
            ' UNION SELECT user1 as user FROM friend WHERE user2 = %s and acceptStatus = "accepted")'
    cursor.execute(query, (lastlogin, username, username, username))
    review_album = cursor.fetchall()
    result['review_album'] = review_album
    cursor.close()
    return result

def get_new_songs(username, lastlogin):
    cursor = conn.cursor()
    query = 'SELECT * ' \
            'FROM song NATURAL JOIN artistperformssong NATURAL JOIN artist ' \
            'WHERE song.releaseDate > %s ' \
            'AND artistID in' \
            '(SELECT artistID ' \
            'FROM userfanofartist ' \
            'WHERE username = %s)'

    cursor.execute(query, (lastlogin, username))
    result = cursor.fetchall()
    cursor.close()
    return result