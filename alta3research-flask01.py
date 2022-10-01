#!/usr/bin/env python3


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
# A list of dictionary 
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


def index():
  # when the key username has a value in session
  if "username" in session:
    username = session["username"]
    return "Logged in as " + username + "<br>" + \
      "<b><a href = '/logout'>click here to log out</a></b>"

  # when the key username does not have a value in session
  return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"


@app.route("/login", methods = ["GET", "POST"])
def login():
   
   if request.method == "POST":

      
      session["username"] = request.form.get("username")
      return redirect(url_for("index"))

   # html data is sent if a get request is received
   return """
   <form action = "" method = "post">
      <p><input type = text name = username></p>
      <p><input type = submit value = Login></p>
   </form>
  """

@app.route("/logout")
def logout():
# delete the username from the session if it is present
   session.pop("username", None)
   return redirect(url_for("index"))



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)









