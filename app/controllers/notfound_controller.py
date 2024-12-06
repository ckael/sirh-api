from flask import render_template

class NotfoundController:
    def index(self):
        return render_template("404 /index.html")
