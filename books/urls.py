from django.urls import path
from books.views import BookViewSet, AuthorViewSet # BookListAPIView, BookDetailView, BookCreateView, BookUpdateView, AuthorListView,
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('books', BookViewSet, basename='book')
router.register('authors', AuthorViewSet, basename='author')

urlpatterns = router.urls