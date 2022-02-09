# flask-restx-boilerplate

The flask-restx-boilerplate allows you to create fast a Flask API application.

Besides that there is an How-To for beginners in the Wiki, which explains step by step how to add a new API Endpoint

The code is mainly based on the following repo [cosmic-byte/flask-restplus-boilerplate](https://github.com/cosmic-byte/flask-restplus-boilerplate) and a little bit from
[antkahn/flask-api-starter-kit](https://github.com/antkahn/flask-api-starter-kit)

There are the following differences in the repositories aboth:

- The tutorials are a little bit outdated and work no longer correctly
- The package versions are outdated and no longer match the tutorial
- This repository combines the best of both (for my understanding)
- Use Flask CLI instead of manager (nativ)
- Use no makefiles (All os friendly)

# Development

[![Python 3.9](https://img.shields.io/badge/python-3.9.10-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-blue.svg)](https://github.com/psf/black)
[![Linter: flake8](https://img.shields.io/badge/code%20style-flake8-blue.svg)](https://github.com/PyCQA/flake8)

# Install / Quickstart

## Dependencies

### Local dependencies

[python 3.9.10](https://www.python.org)

## Full How-To

[Wiki How-To](https://github.com/Ezak91/flask-restx-boilerplate/wiki#how-to)

## Quickstart

### setup project

1. clone this repository

   ```bash
   git clone https://github.com/Ezak91/flask-restx-boilerplate
   ```

1. change to directory

   ```bash
   cd flask-restx-boilerplate
   ```

1. creat venv

   ```bash
   # windows
   py -3 -m venv .venv

   # on linux/mac
   python3 -m venv .venv
   ```

1. activate venv

   ```bash
   # windows
   .venv\scripts\activate

   # on linux/mac
   source .venv/bin/activate
   ```

1. install requirements

   ```bash
   # for developing
   pip install -r requirements-dev.txt
   # only run
   pip install -r requirements.txt
   ```

1. setup flask application

   ```bash
   # bash (linux, mac)
   export FLASK_APP=run
   # bash (windows)
   set FLASK_APP=run
   # powershell (windows)
   $env:FLASK_APP = "run"
   ```

1. setup database

   ```bash
   flask db init
   flask db migrate -m "Initial migration."
   flask db upgrade
   ```

### run flask

1. setup flask application

   ```bash
   # bash (linux, mac)
   export FLASK_APP=run
   # bash (windows)
   set FLASK_APP=run
   # powershell (windows)
   $env:FLASK_APP = "run"
   ```

1. run flask application

   ```bash
   flask run
   ```
   
1. Now you can open the following url in your browser to see the swagger ui page

   ```
   http://127.0.0.1:5000
   ```
