from django.shortcuts import render, redirect, resolve_url
from django.http import HttpResponse
from . import database
import google_auth_oauthlib
from . import CURSOR, CAT_CONN
from googleapiclient.discovery import build
import random


def index(request):
    context = {
        'posts': [x for x in database.get_all_posts()]
    }
    return render(request, 'posts_page.html', context=context)


def login(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/userinfo.email'])
    flow.redirect_uri = 'http://127.0.0.1:8000/posts/oauth'
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
        prompt='consent')
    return redirect(authorization_url)


def oauth(request):
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        'client_secret.json',
        scopes=['https://www.googleapis.com/auth/userinfo.email'],
        state=request.GET['state']
    )
    flow.redirect_uri = "http://127.0.0.1:8000/posts/oauth"

    authorization_response = request.build_absolute_uri()
    flow.fetch_token(authorization_response=authorization_response)
    credentials = flow.credentials
    request.session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

    with build('oauth2', 'v2', credentials=credentials) as userinfo:
        email = userinfo.userinfo().get().execute()['email']

    request.session["email"] = email

    CURSOR.execute("SELECT idusers FROM catposting.users WHERE email = %s", (email,))
    user_id = CURSOR.fetchone()
    if user_id is None:
        user_id = random.Random().randint(0, 2147483647)
        CURSOR.execute("INSERT INTO catposting.users (idusers, email) VALUES (%s, %s)", (user_id, email))
        CAT_CONN.commit()
    return redirect("/posts/")


def post(request):
    if request.session.get('email', 'none') == 'none':
        return redirect('/posts/login')
    else:
        return render(request, 'create_post.html')


def post_submit(request):
    email = request.session.get('email', 'none')
    file = request.FILES.get('image')
    title = request.POST.get('title', '')
    file_id = random.Random().randint(0, 2147483647)
    with open(f"media/{file_id}.jpg", "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    print(email)
    print(file)
    print(title)
    CURSOR.execute("INSERT INTO catposting.posts (post_id, title, cat, likes) VALUES (%s, %s, 0, 5)", (file_id, title))
    CAT_CONN.commit()
    return redirect('/posts/')