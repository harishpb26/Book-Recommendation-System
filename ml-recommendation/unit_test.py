import unittest
import json
import requests
from app import app, db
from urllib.parse import quote

# no of recommendations
nrecommends = 10
# no of books returned in multistage download
size = 15

class FlaskTestCase(unittest.TestCase):

    # /recommend/{title}
    def test_to_recommend(self):
        title = "The Hobbit"
        response = requests.get('http://localhost:5000/recommend/{recommendTitle}'.format(recommendTitle = quote(title)))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['books']), nrecommends)

    def test_to_recommend_invalid_method(self):
        response = requests.delete('http://localhost:5000/recommend/{recommendTitle}'.format(recommendTitle = "The Ultimate Hitchhiker's Guide to the Galaxy"))
        self.assertEqual(response.status_code, 405)

    def test_to_recommend_invalid_url(self):
        title = "Harry Potter Collection (Harry Potter, #1-6)"
        response = requests.get('http://localhost:5000/recommend/{recommendTitle}'.format(recommendTitle = title))
        self.assertEqual(response.status_code, 400)

    # /books
    def test_list_books_invalid_method(self):
        info = {"index": 0, "size": size}
        response = requests.put('http://localhost:5000/books', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 405)

    def test_list_books(self):
        info = {"index": 0, "size": size}
        response = requests.post('http://localhost:5000/books', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['books']), size)

    def test_list_books_count(self):
        info = {"index": 990, "size": size}
        response = requests.post('http://localhost:5000/books', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(len(response.json()['books']), size + 10)

    def test_list_books_invalid_index(self):
        info = {"index": 1001, "size": size}
        response = requests.post('http://localhost:5000/books', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(len(response.json()['books']), 0)

    # /add_book
    def test_insert_book_empty_title(self):
        info = {"title": "", "authors": "HCVerma", "average_rating": 5}
        response = requests.post('http://localhost:5000/add_book', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['books'], "")

    def test_insert_book_empty_authors(self):
        info = {"title": "covid19", "authors": "", "average_rating": 1}
        response = requests.post('http://localhost:5000/add_book', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['books'], "")

    def test_insert_book(self):
        info = {"title": "unittest", "authors": "Host", "average_rating": 4}
        response = requests.post('http://localhost:5000/add_book', data=json.dumps(info), headers={'Content-Type': 'application/json'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['books'][0]['title'], info["title"])
        self.assertEqual(response.json()['books'][0]['authors'], info["authors"])
        self.assertEqual(response.json()['books'][0]['average_rating'], info["average_rating"])

if __name__ == '__main__':
    unittest.main()
