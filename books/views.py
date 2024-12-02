from datetime import timezone

from rest_framework.generics import (ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView,
                                     ListCreateAPIView
                                     )
from rest_framework.viewsets import ModelViewSet

from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer, BookCreateSerializer


# class BookListAPIView(ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetailView(RetrieveAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookCreateView(CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookCreateSerializer
#
#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user.username)
#
#
# class BookUpdateView(UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookCreateSerializer
#
#     def perform_update(self, serializer):
#         serializer.save(updated_at=timezone.now())
#
#
# class BookDeleteView(DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class AuthorListView(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

