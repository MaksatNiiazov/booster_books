from django.urls import path
from books.views import BookListAPIView, BookDetailView, BookCreateView, BookUpdateView, AuthorListView

urlpatterns = [
    path('', BookListAPIView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('authors/', AuthorListView.as_view(), name='authors'),

    # path('books/<int:pk>/delete/', BookDetailView.as_view(), name='book-delete'),

]

