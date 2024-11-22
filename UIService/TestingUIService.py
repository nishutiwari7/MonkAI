import unittest
from unittest.mock import patch
from app import app

class TestUIService(unittest.TestCase):
    def setUp(self):
        """Set up test client and initialize the Flask test environment."""
        self.app = app.test_client()
        self.app.testing = True

    def test_index_page(self):
        """Test that the index page loads successfully."""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Upload an Image for Object Detection', response.data)

    @patch('requests.post')
    def test_image_upload_success(self, mock_post):
        """Test successful image upload and response from AI service."""
        # Mock the AI service response
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "detections": [
                {"class": "person", "confidence": 0.98, "bounding_box": [100, 50, 200, 150]},
                {"class": "dog", "confidence": 0.87, "bounding_box": [50, 100, 150, 200]}
            ],
            "output_image": "output/images/test_image.jpg"
        }

        with open('test_image.jpg', 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n')  # Simulating an image file for testing

        with open('test_image.jpg', 'rb') as img:
            response = self.app.post(
                '/',
                data={'image': img},
                content_type='multipart/form-data'
            )

        self.assertEqual(response.status_code, 200)
        self.assertIn(b'detections', response.data)
        self.assertIn(b'person', response.data)
        self.assertIn(b'dog', response.data)

    @patch('requests.post')
    def test_image_upload_error(self, mock_post):
        """Test handling of errors from the AI service."""
        # Mock the AI service response for an error
        mock_post.return_value.status_code = 500
        mock_post.return_value.text = "Internal Server Error"

        with open('test_image.jpg', 'wb') as f:
            f.write(b'\x89PNG\r\n\x1a\n')  # Simulating an image file for testing

        with open('test_image.jpg', 'rb') as img:
            response = self.app.post(
                '/',
                data={'image': img},
                content_type='multipart/form-data'
            )

        self.assertEqual(response.status_code, 500)
        self.assertIn(b"Error", response.data)

    def test_no_file_upload(self):
        """Test the case where no file is uploaded."""
        response = self.app.post(
            '/',
            data={},
            content_type='multipart/form-data'
        )
        self.assertEqual(response.status_code, 400)
        self.assertIn(b"No file uploaded", response.data)

if __name__ == '__main__':
    unittest.main()
