from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']


class BookCreateSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'published_date']


class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    books_count = serializers.SerializerMethodField()
    qwe = serializers.SerializerMethodField()
    first_published_date = serializers.SerializerMethodField()

    class Meta:
        model = Author
        fields = ['id', 'qwe', 'name', 'books_count', 'first_published_date', 'biography', 'books']

    def get_qwe(self, obj):
        return '1321313213213'

    def get_books_count(self, obj):
        return obj.books.count()

    def get_first_published_date(self, obj):
        first_book = obj.books.order_by('published_date').first()
        return first_book.published_date if first_book else None
