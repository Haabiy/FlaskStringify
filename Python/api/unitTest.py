from api import app
from flask import json
import unittest

class TestAPI(unittest.TestCase):
    """This class defines test cases for the API."""
    
    def setUp(self):
        """Setup method to initialize the Flask test client."""
        self.app = app.test_client()

    def test_string(self):
        """Test case to check if the API endpoint '/clean_string' works correctly."""
        input_data = {"string": "2076,3B,19C,138D,NULL,NULL"}
        expected_result = {"cleaned_string": "138D,19C,3B,2076"}
        response = self.app.post('/clean_string', json=input_data)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data, expected_result)

if __name__ == '__main__':
    unittest.main()
