from flask import Flask

app = Flask(__name__)

app.secret_key = "this is my belt exam"

DATABASE = "tv_shows"