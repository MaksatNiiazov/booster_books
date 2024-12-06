from django.urls import path

from books.views import BookViewSet, AuthorViewSet, \
    BookListView  # BookListAPIView, BookDetailView, BookCreateView, BookUpdateView, AuthorListView,
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', BookViewSet, basename='book')
router.register('authors/', AuthorViewSet, basename='author')

urlpatterns = router.urls

# urlpatterns = [
#         path('', BookListView.as_view(), name='book_list'),
#     ]