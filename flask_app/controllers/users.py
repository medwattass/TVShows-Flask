from flask import render_template, redirect, session, request, flash
from flask_app import app
from flask_app.models.tv_show import Tv_show
from flask_app.models.user import User
from flask_app.models.like import Like
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)


#===================Main page==============================
@app.route('/')
def index():
    return render_template('index.html')


#===================Registration method==============================
@app.route('/register', methods=['POST'])
def register():
    if not User.validate_registration(request.form):
        return redirect('/')
    data ={ 
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    session['user_id'] = User.save_user(data)
    return redirect('/shows')


#===================Login method==============================
@app.route('/login', methods=['POST'])
def login():
    user = User.get_user_by_email(request.form)
    if not user:
        flash("Email doesn't exist in the Database", "login")
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("Invalid Password", "login")
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/shows')


#===================This method take you to the Shows page==============================
@app.route('/shows')
def shows():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    user = User.get_user_by_id(data)
    tv_shows = Tv_show.get_all_tv_shows()
    
    tv_show_liked = {}
    
    for tv_show in tv_shows:
        liked_data ={
            'user_id': session['user_id'],
            'tv_show_id': tv_show.id
        }
        liked_by_current_user = Like.check_like(liked_data)
        tv_show_liked.update({tv_show.id : liked_by_current_user})

    return render_template("shows.html", user=user, tv_shows=tv_shows, tv_show_liked=tv_show_liked)


#===================The logout method==============================
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')