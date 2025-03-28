# oauth.py
from flask import redirect, url_for, session, request, flash
from flask_oauthlib.client import OAuth
import os
from app import app, db, User
from werkzeug.security import generate_password_hash

oauth = OAuth(app)

# Configure Google OAuth
google = oauth.remote_app(
    'google',
    consumer_key=os.environ.get('GOOGLE_CLIENT_ID', 'your-google-client-id'),
    consumer_secret=os.environ.get('GOOGLE_CLIENT_SECRET', 'your-google-client-secret'),
    request_token_params={
        'scope': 'email profile'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

# Configure GitHub OAuth
github = oauth.remote_app(
    'github',
    consumer_key=os.environ.get('GITHUB_CLIENT_ID', 'your-github-client-id'),
    consumer_secret=os.environ.get('GITHUB_CLIENT_SECRET', 'your-github-client-secret'),
    request_token_params={'scope': 'user:email'},
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url='https://github.com/login/oauth/authorize'
)

@app.route('/login/google')
def login_google():
    return google.authorize(callback=url_for('authorized_google', _external=True))

@app.route('/login/github')
def login_github():
    return github.authorize(callback=url_for('authorized_github', _external=True))

@app.route('/login/authorized/google')
def authorized_google():
    resp = google.authorized_response()
    if resp is None or resp.get('access_token') is None:
        flash('Authentication failed')
        return redirect(url_for('login'))

    session['google_token'] = (resp['access_token'], '')
    user_info = google.get('userinfo')

    # Check if user exists
    user = User.query.filter_by(email=user_info.data['email']).first()
