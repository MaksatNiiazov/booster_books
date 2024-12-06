from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import OrderingFilter
from .filters import BookFilter
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, BookCreateSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['author', 'genre', 'published_date']
    filterset_class = BookFilter
    ordering_fields = ['title', 'published_date']


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(APIView):

    def get(self, request):
        queryset = Book.objects.all()
        author = request.query_params.get('author')  # Получение параметра author
        genre = request.query_params.get('genre')  # Получение параметра genre
        if author:
            queryset = queryset.filter(author__name__icontains=author)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)

        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)


class BooksListApiView(ListAPIView):
    model = Book
    queryset = Book.objects.all()
    serializer_class = BookSerializer

