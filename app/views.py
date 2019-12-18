from app import app, db
from flask import render_template, request, redirect, flash
from .models import Post
from .forms import AddPostForm

@app.route('/')
@app.route('/home')
def index():
    posts = Post.query.all()
    return render_template('post.html', posts=posts)

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html', user_name='allen Zhao')
