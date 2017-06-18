from django.test import TestCase
from .models import Post


class PostTests(TestCase):
    # Test for our Post model
    def test_str(self):
        # Test title of Blog post
        test_title = Post(title='My Latest Blog Post')
        self.assertEqual(str(test_title), 'My Latest Blog Post')
