
# Authentication For Lushlyrics
This task is a part of my coursera learning journey where i had to implement authentication for a music website, 

## Features
- Login
  User inputs username and password and logs in to access music dir
- SignUp
  User signs up with username, password, email to get access
- Logout
  User clears session by login out, after logout, user can not access website
- Email Verification
  This is part of the registration process where the user verifies their email
- View Protection
  This is an advanced feature that limits access to routes by protecting them 
## Setup

To get this project setup on your system for testing, please follow the following steps

- You can decide to fork the repository or

```sh
$ git clone https://github.com/andy21-mch/Lushlyrics-insecure.git
$ cd Lushlyrics-insecure/lushlyrics-webapp-django
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python3 -m venv your_env
$ source your_env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(your_env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(your_env)$ cd cd Lushlyrics-insecure/lushlyrics-webapp-django
(your_env)$ python manage.py runserver

```
And navigate to `http://127.0.0.1:8000/`.