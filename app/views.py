from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm
from noteData import note


from firebase import firebase
firebase = firebase.FirebaseApplication('https://thoughtspace.firebaseio.com/', None)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Whats your note'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'add it'}, 
            'body': 'Add your note here' 
        },

    ]
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

@app.route('/newNote/<typeF>/<contents>')
def makeNote(typeF,contents):
  nNote=note(typeF,contents)
  #thoughtspace.firebase.io
  #make call to firebase
  note_id=1
  contentDict={'type':typeF, 'content':contents}
  firebase.post("/notes",contentDict )
  return render_template("newNote.html",
                          typef=nNote.getType(),
                          content=nNote.getContent())


