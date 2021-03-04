# Book-Recommendation-System

## Introduction

Book recommendation system that uses Content-based filtering to recommend books to the user based on the selected book. AJAX Pattern Multi-Stage download is implemented in React. Built-in Python module unittest is used to implement unit tests. The user can 
* Add new book into the database
* View the list of books stored in the database
* Get recommendations similar to the selected book

## Multi-Stage Download

AJAX Pattern Multi-Stage download is implemented in React. The navigation bar is initially loaded onto the page. The books are loaded in chunks. First, say k books are loaded onto the page. Then after some time interval, the next k books are loaded onto the page and so on. This ensures there is less load onto the server.

## Setup

To clone and run this application, you'll need Git, Python3, Flask, Node and React installed on your machine. From your command line:
1. Clone this repository <br> `$ git clone https://github.com/harishpb26/Book-Recommendation-System`

2. Go into the repository <br> `$ cd Book-Recommendation-System`

3. Go into ml-recommendation <br> `$ cd ml-recommendation`

4. Run flaskapp app.py <br> `$ python3 app.py`

5. Go into react-book-recommendation <br> `$ cd react-book-recommendation`

6. Install node modules <br> `$ npm install`

7. Run npm start <br> `$ npm start`

8. Access react-app on http://localhost:3000
