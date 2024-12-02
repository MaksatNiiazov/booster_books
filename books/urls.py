from django.urls import path
from books.views import BookListAPIView, BookDetailView, BookCreateView, BookUpdateView, AuthorListView, BookViewSet, AuthorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('authors', AuthorViewSet, basename='author')

urlpatterns = router.urls



class Dog:
    pass

dog1 = Dog()