import unittest
import os
from app import app

class TestAIService(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_no_image(self):
        response = self.app.post('/detect', data={})
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"No image provided", response.data)

    def test_image_upload(self):
        with open("test_image.jpg", "rb") as img:
            response = self.app.post('/detect', data={"image": img})
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"detections", response.data)

if __name__ == "__main__":
    unittest.main()
