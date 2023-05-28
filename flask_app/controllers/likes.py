from flask import render_template, redirect, session, request
from flask_app import app
from flask_app.models.like import Like


@app.route('/shows/like/<int:user_id>/<int:tv_show_id>')
def like_tv_show(user_id, tv_show_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "user_id": user_id,
        "tv_show_id": tv_show_id
    }
    Like.add_a_like(data)
    return redirect('/shows')


@app.route('/shows/unlike/<int:user_id>/<int:tv_show_id>')
def unlike_tv_show(user_id, tv_show_id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "user_id": user_id,
        "tv_show_id": tv_show_id
    }
    Like.remove_a_like(data)
    return redirect('/shows')