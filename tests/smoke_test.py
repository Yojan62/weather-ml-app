import warnings
warnings.filterwarnings("ignore")

import unittest
from app import app

class TestAppSmoke(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.client = app.test_client()
    
    # Test a success in running the application
    def test_prediction_route_success(self):
        response = self.client.get('/')
        # CHECK: Status code should be 200 (OK)
        self.assertEqual(response.status_code, 200)

    # Test a form is rendered
    def test_get_form(self):
        response = self.client.get('/')
        # CHECK: The HTML should contain the form title
        self.assertIn(b'Weather Classification', response.data)
 
if __name__ == '__main__':
    unittest.main()