from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Like:
    def __init__(self, data_base):
        self.id = data_base['id']
        self.user_id = data_base['user_id']
        self.tv_show_id = data_base['tv_show_id']
    
    #===================Add a like for a TV Show==============================
    @classmethod
    def add_a_like(cls, data):
        query = "INSERT INTO likes (user_id, tv_show_id) VALUES (%(user_id)s, %(tv_show_id)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Remove a like from a TV Show==============================
    @classmethod
    def remove_a_like(cls, data):
        query = "DELETE FROM likes WHERE user_id = %(user_id)s AND tv_show_id = %(tv_show_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Get total TV Show likes by it's id==============================
    @classmethod
    def get_total_likes(cls, data):
        query = "SELECT COUNT(*) AS likes_count FROM likes WHERE tv_show_id = %(tv_show_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Check if the User already liked the TV Show==============================
    @classmethod
    def check_like(cls, data):
        query = "SELECT * FROM likes WHERE user_id = %(user_id)s AND tv_show_id = %(tv_show_id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Delete likes related to a TV Show==============================
    @classmethod
    def delete_likes(cls, data):
        query = "DELETE FROM likes WHERE tv_show_id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)