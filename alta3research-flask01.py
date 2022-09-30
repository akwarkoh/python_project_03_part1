#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify
from flask import render_template
from flask import make_response
from flask import url_for
from flask import session
from flask import escape



app = Flask(__name__)

menu = [{
    "meal": "Waakye and fried fish",
    "country": "Ghana",
    "calories": 700,
    "ingredients": ["beans", "rice", "tomatoes", "fish", "oil", "salt"]
             },
        {
    "meal": "Moules Frites",
    "country": "Belgium",
    "calories": 603,
    "ingredients": ["mussels", "creme fraiche", "butter", "minced chives", "garlic", "olive oil", "salt"]
             },

         {
    "meal": "Poutine",
    "country": "Canada",
    "calories": 510,
    "ingredients": ["beef gravy", "vegetable oil", "potatoes", "cheese curds"]
             }    

             ]

@app.route("/")
def index():
    
    # returns menu as a json data
   return jsonify(menu)

#@app.route("/")
def index():

  if "username" in session:
    username = session["username"]
    return "Logged in as " + username + "<br>" + \
      "<b><a href = '/logout'>click here to log out</a></b>"

  
  return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"


@app.route("/login", methods = ["GET", "POST"])
def login():
   
   if request.method == "POST":

      
      session["username"] = request.form.get("username")
      return redirect(url_for("index"))

   
   return """
   <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route("/logout")
def logout():

   session.pop("username", None)
   return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)









