from rest_framework.viewsets import ModelViewSet

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, BookCreateSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
