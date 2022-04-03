from turtle import title

from django.contrib.auth.models import User
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        test_user_1 = User.objects.create_user(username="testuser1", password="abc123")
        test_user_1.save()

        test_post_1 = Post.objects.create(
            author=test_user_1, title="test title", body="test body"
        )
        test_post_1.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f"{post.author}"
        title = f"{post.title}"
        body = f"{post.body}"
        self.assertEqual(author, "testuser1")
        self.assertEqual(title, "test title")
        self.assertEqual(body, "test body")
