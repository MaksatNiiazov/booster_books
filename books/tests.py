from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Создание тестового пользователя
        self.user = User.objects.create_user(username="testuser", password="testpassword")

        self.author = Author.objects.create(name="George Orwell", biography="Author of 1984")
        # Создание тестовой книги
        self.book = Book.objects.create(
            title="1984",
            author=self.author,
            published_date="1949-06-08",
            genre="Sci-Fi",
        )

        # URL для API книг
        self.url = "/books/"

    def test_get_books(self):
        # Отправляем GET-запрос к /api/books/
        response = self.client.get(self.url)
        # Проверяем статус ответа
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Проверяем, что возвращается одна книга
        self.assertEqual(len(response.data), 4)
        # Проверяем данные книги
        self.assertEqual(response.data['results'][0]["title"], "1984")
        self.assertEqual(response.data['results'][0]["author"], "George Orwell")
        self.assertEqual(response.data['results'][0]["published_date"], "1949-06-08")
        self.assertEqual(response.data['results'][0]["genre"], "Sci-Fi")
