## Setup

The first thing to do is to clone the repository:

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