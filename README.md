# My Personal Kanban API
My Personal Kanban is exactly that, your very own Kanban Board! You can add cards to your to-do list, move them to being in progress, and then file them under complete so you know when to start the next task. Great for project managers who use agile and scrum methodologies or for anyone who just likes to check things off their to-do list. This is the Django-Python API for this application that connects it to it's SQL database.

## Links
- [Client Repo](https://github.com/bchin224/my_personal_kanban_client)
- [Deployed Client](https://bchin224.github.io/my_personal_kanban_client/)
- [Deployed Backend](https://mypersonalkanban22321.herokuapp.com/)

## Planning Process & Problem-Solving Strategy
2/17
- Setting up Django API
- Built card model, card_views, and card serializer
- Added card and card detail urls in api
- Made curl scripts for cards (running into DEBUG = True error)

2/18
- Fixed psycopg2 install issue in pipfile
- Added Procfile for pre-deployment
- Adjusted serializer to include primary keys as id's for index, show and update
- Added '/' for all curl script url's to fix 301 errors. All curl scripts now functional
- Deployed app to heroku

2/22
- Remove reference data
- Updating readme and finishing touches

## Install Preparation
1. Fork and clone this repository.
2. Create and checkout to a new branch for your work.
3. Run `pipenv shell` to start up your virtual environment.
4. Run `pipenv install` to install dependencies.
5. Create a psql database for the project
    1. Type `psql` to get into interactive shell
    2. Run `CREATE DATABASE "<your_name>_kanban";`
    3. Exit shell
6. Generate and run migrations with `python3 manage.py makemigrations` and `python3 manage.py migrate`
7. Run the server with `python3 manage.py runserver`

## Routes
| Verb     | URI Pattern | Controller # Action|
| -------- |:-----------:| ------------:|
| POST     | /           | cards#create |
| GET      | /cards      | cards#index  |
| PATCH    | /cards/:id  | cards#update |
| DELETE   | /cards/:id  | cards#delete |

## Technologies
- Django
- Python
- Heroku

## Entity Relationship Diagram
![Imgur](https://i.imgur.com/l47P8fj.jpg)

## Unsolved Problems
- Would like to allow a user to save multiple kanban boards for multiple projects, thus requiring a new model for kanban boards that have a one to many relationship with the cards model
