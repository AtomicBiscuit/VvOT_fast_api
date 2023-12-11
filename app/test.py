from unittest.case import TestCase
from fastapi.testclient import TestClient
from app.fastapi_module import app


class BaseCase(TestCase):
    """
    Базовый класс для генерации тестов
    """

    def setUp(self) -> None:
        self.client = TestClient(app)


class RequestGetTestCase(BaseCase):
    """
    Класс тестирования get-запросов
    """

    def test_root_page_request_message(self) -> None:
        self.assertDictEqual(self.client.request('get', '').json(), {'message': 'Привет, жестокий мир'})
