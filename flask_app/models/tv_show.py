from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Tv_show:
    def __init__(self, data_base):
        self.id = data_base['id']
        self.user_id = data_base['user_id']
        self.title = data_base['title']
        self.network = data_base['network']
        self.release_date = data_base['release_date']
        self.description = data_base['description']
        self.created_at = data_base['created_at']
        self.updated_at = data_base['updated_at']
    
    #===================Saving a TV Show==============================
    @classmethod
    def save_tv_show(cls, data):
        query = "INSERT INTO tv_shows (user_id, title, network, release_date, description) VALUES (%(user_id)s, %(title)s, %(network)s, %(release_date)s, %(description)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Getting all TV Shows in the DB==============================
    @classmethod
    def get_all_tv_shows(cls):
        query = "SELECT * FROM tv_shows;"
        results =  connectToMySQL(DATABASE).query_db(query)
        all_tv_shows = []
        for row in results:
            all_tv_shows.append( cls(row) )
        return all_tv_shows
    
    #===================Getting one TV Show by id==============================
    @classmethod
    def get_one_tv_show(cls, data):
        query = "SELECT * FROM tv_shows WHERE id = %(id)s;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls( results[0] )
    
    #===================Updating a TV Show by id==============================
    @classmethod
    def update_tv_show(cls, data):
        query = "UPDATE tv_shows SET title=%(title)s, network=%(network)s, release_date=%(release_date)s, description=%(description)s WHERE id=%(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Delete a TV Show by id==============================
    @classmethod
    def delete_tv_show(cls, data):
        query = "DELETE FROM tv_shows WHERE tv_shows.id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    #===================Validate TV Show for creation or updating==============================
    @staticmethod
    def validate_tv_show(tv_show):
        is_valid = True
        if len(tv_show['title']) < 3:
            is_valid = False
            flash("Title must be at least 3 characters","tv_show")
        if len(tv_show['network']) < 3:
            is_valid = False
            flash("Network must be at least 3 characters","tv_show")
        if len(tv_show['description']) < 3:
            is_valid = False
            flash("Description must be at least 3 characters","tv_show")
        if tv_show['release_date'] == "":
            is_valid = False
            flash("Please enter a release date","tv_show")
        return is_valid