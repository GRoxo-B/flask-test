import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from app import app

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Index Page')

    def test_hello_world(self):
        response = self.app.get('/hello')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

    def test_show_user_profile(self):
        response = self.app.get('/user/testuser')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'testuser', response.data)

    def test_get_json(self):
        response = self.app.get('/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {
            'name': 'John Doe',
            'age': 30,
            'city': 'New York'
        })

    def test_set_cookie(self):
        response = self.app.get('/setcookie')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Cookie is set')
        self.assertIn('username', response.headers.get('Set-Cookie'))

    def test_get_cookie(self):
        self.app.set_cookie('username', 'john_doe')
        response = self.app.get('/getcookie')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Username is john_doe', response.data)

    def test_404_error_handler(self):
        response = self.app.get('/nonexistent')
        self.assertEqual(response.status_code, 404)
        self.assertIn(b'Page Not Found', response.data)
        self.assertEqual(response.headers.get('X-ERROR'), 'ERRO 404')

if __name__ == '__main__':
    unittest.main()