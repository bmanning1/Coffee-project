from django.test import TestCase
from home.views import get_index
from django.core.urlresolvers import resolve
from django.shortcuts import render_to_response
from accounts.models import User


class HomePageTest(TestCase):
    def setUp(self):
        # Test to set up a User
        super(HomePageTest, self).setUp()
        self.user = User.objects.create(username='testuser')
        self.user.set_password('password')
        self.user.save()
        self.login = self.client.login(username='testuser',
                                       password='password')
        self.assertEqual(self.login, True)

    def test_home_page_resolves(self):
        # Test the Home page
        home_page = resolve('/')
        self.assertEqual(home_page.func, get_index)

    def test_home_page_status_code_is_ok(self):
        # Test Home page Status Code
        home_page = self.client.get('/')
        self.assertEqual(home_page.status_code, 200)

    def test_check_content_is_correct(self):
        # Test Home page content
        home_page = self.client.get('/')
        self.assertTemplateUsed(home_page, "index.html")
        home_page_template_output = render_to_response("index.html", {'user': self.user}).content
        self.assertEqual(home_page.content, home_page_template_output)
