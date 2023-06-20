# My-store
## :orange_book: Description
My repo from course https://rest-apis-flask.teclado.com/
REST APIs with Flask and Python is a complete course that teaches you how to develop complete, professional REST APIs using Flask, PostgreSQL, and Docker.
## :heavy_check_mark: Pre-requisites
 - Python 3.9
## :floppy_disk: Installation
We recommend using a virtual environment.
```sh
pip install -r requirements.txt
```
## Enviroment variables
| variable    | value | comment |
|-------------|-------|---------|
| FLASK_APP   | app   |         |
| FLASK_DEBUG | True  |         |
## :runner: Run the API
```sh
flask run
```
## :whale: Docker
You could also run the app within a Docker container.
### Build the image
```sh
docker build -t my-store .
```
### Run the container image
```sh
docker run -d my-store
```
## Contribute
### Pre-commit
```sh
pre-commit install
```
