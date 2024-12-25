from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend, OrderingFilter
from rest_framework.filters import OrderingFilter
from .filters import BookFilter
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, BookCreateSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from rest_framework.filters import SearchFilter
from rest_framework.authtoken.models import Token



class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter, SearchFilter]
    filterset_fields = ['author', 'genre', 'published_date']
    filterset_class = BookFilter
    ordering_fields = ['title', 'published_date']
    permission_classes = [AllowAny]
    search_fields = ['title', 'author']


class AuthorViewSet(ModelViewSet, LoginRequiredMixin):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookListView(APIView, LoginRequiredMixin):

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

