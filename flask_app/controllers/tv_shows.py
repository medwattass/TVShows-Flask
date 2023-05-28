from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.tv_show import Tv_show
from flask_app.models.user import User
from flask_app.models.like import Like


#===================Creating a TV Show==============================
@app.route('/shows/new')
def new_show():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    user = User.get_user_by_id(data)
    return render_template('new_show.html', user=user)

@app.route('/create/show', methods=['POST'])
def create_show():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tv_show.validate_tv_show(request.form):
        return redirect('/shows/new')
    data = {
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"],
        "user_id": session['user_id']
    }
    Tv_show.save_tv_show(data)
    return redirect('/shows')


#===================Editing a TV Show==============================
@app.route('/shows/edit/<int:id>')
def edit_tv_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    this_show = Tv_show.get_one_tv_show(data)
    user = User.get_user_by_id(user_data)
    return render_template("edit_tv_show.html", this_show=this_show, user=user)

@app.route('/update/show/<int:id>', methods=['POST'])
def update_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    if not Tv_show.validate_tv_show(request.form):
        return redirect('/shows/new')
    data = {
        "id": id,
        "title": request.form["title"],
        "network": request.form["network"],
        "release_date": request.form["release_date"],
        "description": request.form["description"]
    }
    Tv_show.update_tv_show(data)
    return redirect('/shows')


#===================Showing a TV Show==============================
@app.route('/shows/<int:id>/<int:user_id>')
def show_tv_show(id, user_id):
    if 'user_id' not in session:
        return redirect('/logout')
    
    data = {
        "id":id
    }
    tv_show = Tv_show.get_one_tv_show(data)
    
    poster_data = {
        "id": user_id
    }
    poster_info = User.get_user_by_id(poster_data)
    
    likes_data = {
        "tv_show_id": tv_show.id
    }
    likes_count = Like.get_total_likes(likes_data)
    return render_template("show_tv_show.html", tv_show=tv_show, poster_info=poster_info, likes_count=likes_count)


#===================Deleting a TV Show==============================
@app.route('/shows/delete/<int:id>')
def delete_show(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id": id
    }
    Like.delete_likes(data)
    Tv_show.delete_tv_show(data)
    return redirect('/shows')
