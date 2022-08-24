from django.test import TestCase
from django.http import HttpRequest, HttpResponse
from todolist.views import index


class ViewsTest(TestCase):
    def test_index_returns_correct_html(self) -> None:
        request: HttpRequest = HttpRequest()

        response: HttpResponse = index(request)
        html: str = response.content.decode("utf8")

        self.assertInHTML("SITODO", html)


class UrlsTest(TestCase):
    def test_root_path_returns_index_page(self) -> None:
        response: HttpResponse = self.client.get("/")

        self.assertTemplateUsed(response, "todolist/index.html")
