import unittest
import json
from app import app

class ApiTestCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_greet(self):
        response = self.app.get('/api/greet')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, World!')

    def test_greet_with_name(self):
        response = self.app.get('/api/greet?name=Alice')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['message'], 'Hello, Alice!')

    def test_sum_numbers(self):
        response = self.app.post('/api/sum', data=json.dumps({'numbers': [1, 2, 3, 4]}),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['sum'], 10)

    def test_sum_numbers_empty(self):
        response = self.app.post('/api/sum', data=json.dumps({'numbers': []}),
                                 content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['sum'], 0)

if __name__ == '__main__':
    unittest.main()
