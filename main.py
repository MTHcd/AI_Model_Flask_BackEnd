from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import select

from datetime import datetime, timezone
import bcrypt

# Steps:
# 1. Design and implement a database
#   - SQLite, MySql, Maria
#   - SQLAlchemy
# 2. Connect Database to Flask
# ----------
# 3. Project Design
# 4. Add in Machine Learning
# 5. Connect Machine Learning to Flask
# 6. ???
# 7. Profit < Have a good portfolio project

# Generating a flask App
app = Flask(__name__) # usually ends up as "__main__"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.sqlite"

db = SQLAlchemy(app = app)

with app.app_context():
  db.reflect()

print(list(db.metadata.tables.keys()))

from Models import *

# Decorator that lets flask know what url path this function requires
@app.route("/")
def index():
  users = db.session.execute(db.select(User)).scalars()
  output = ""
  for user in users:
    output += user.email + "<br/>"
  return output # The returned value gets sent directly

# HTTP Methods
# Get : http://server.com/path/to/url?arg=1&arg=2
# - Most Common
# - Send Unencrypted
# - Data is in the url
#
# Post, Put, Patch, Delete
# - Used to send data to the server
# - Data is encrypted in the body
# - Method can be used to indicate desired result

@app.route("/test/<id>", methods=["GET"])
def test(id: int):
  user = db.get_or_404(User, int(id))
  return f"Your email is {user.email}"

# CRUD System
#
# Create  : POST
# Read    : GET
# Update  : PUT
# Delete  : DELETE

# http://server.com/path/to/query/<id>
# query 12: "What is your favorite <value>?"
# POST   : http://server.com/path/to/query -> create a user
# GET    : http://server.com/path/to/query/12 -> view user 12
# PUT    : http://server.com/path/to/query/12 -> change values on user 12
# DELETE : http://server.com/path/to/query/12 -> remove user 12

# E.G. http://server.com/path/to/query/12?value=Movie

@app.route("/api/register", methods=["POST"])
def register():
  try:
    email = request.json["email"]
    password = request.json["password"]

    user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one_or_none()

    if user is not None:
      raise Exception("User already exists")

    # verify the password
    salt = bcrypt.gensalt()
    print(salt.decode())

    hash = bcrypt.hashpw(password.encode(), salt)

    user = User()
    user.email = email
    user.password = hash.decode()
    user.created_at = str(datetime.now())
    user.updated_at = str(datetime.now())

    db.session.add(user)
    db.session.commit()

    return jsonify({"user": user})

  except Exception as e:
    return jsonify({ "error": str(e) })
  
@app.route("/api/authenticate", methods=["POST"])
def authenticate():
  try:
    email = request.json["email"]
    password = request.json["password"]

    user = db.one_or_404(db.select(User).filter_by(email=email))

    # verify the password
    salt = user.password[:29]
    print(salt)

    hash = bcrypt.hashpw(password.encode(), salt.encode())

    # generate the auth token
    if hash != user.password.encode():
      raise Exception("Invalid Email/Password")

    return jsonify({"token": "INSERT-TOKEN-HERE"})

  except Exception as e:
    return jsonify({ "error": str(e) })

@app.route("/api/session", methods=["POST"]) # Create
def create_session():
  try:
    headers = request.headers
    auth = headers.get("Authentication")

    session = Session()
    session.user_id = auth
    session.model_id = request.json["model_id"]
    session.created_at = str(datetime.now(timezone.utc))
    session.updated_at = str(datetime.now(timezone.utc))
    
    db.session.add(session)
    db.session.commit()

    return jsonify({ "session_id": session.id })

  except Exception as e:
    return jsonify({ "error": e })

@app.route("/api/session", methods=["GET"]) # Read-multiple
def list_sessions():
  pass

@app.route("/api/session/<id>", methods=["GET"]) # Read-single
def read_session(id: int):
  pass

@app.route("/api/session/<id>", methods=["PUT"]) # Update
def update_session(id: int):
  pass

@app.route("/api/session/<id>", methods=["DELETE"]) # Delete
def delete_session(id: int):
  pass

@app.route("/api/session/<id>/request", methods=["POST"]) # Make Request
def make_request(id: int):
  pass

# API: Application Programming Interface
# - Code someone else(or yourself) wrote to do a task and you're calling it
# - Package, Module, Library, SDK (usually means tools are included)

# If we're running this code directly then 
if __name__ == "__main__":
  # Start our Flask App
  app.run()