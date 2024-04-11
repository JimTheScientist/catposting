# Overview

I created this repository to aid in learning Django.

When in the catposting directory, run ```python manage.py runserver```.

[Software Demo Video](https://www.youtube.com/watch?v=LwHHzxlcuBI)

# Web Pages

/posts/ is the main posts page. It updates with all the posts that users add to the site.
/posts/post is the page to create a new post. This is where user input is added.
/posts/login is the login page, you can log in with google.

# Development Environment


You need a MySQL server running in order to use this. 
You need to set up a google OAuth endpoint in order to use this, and to put the client_secret.json in the catposting directory.
You must have Django, Jinja2, mysql-connector-python, and the google-api and google-auth libraries.

# Useful Websites

* [Google OAuth2 Overview](https://developers.google.com/identity/protocols/oauth2)
* [Oauth2 examples](https://developers.google.com/identity/protocols/oauth2/javascript-implicit-flow)

# Future Work

- Add "cats" feature, which lets users post under cat pseudonyms.
- Add comment feature
- Make the likes button work.
