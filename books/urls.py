from django.urls import path

from books.views import BookViewSet, AuthorViewSet, \
    BookListView  # BookListAPIView, BookDetailView, BookCreateView, BookUpdateView, AuthorListView,
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register('books', BookViewSet, basename='book')

router.register('authors/', AuthorViewSet, basename='author')

urlpatterns = router.urls

urlpatterns += [

]
