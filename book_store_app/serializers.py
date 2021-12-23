from book_store_app.models import Category, Book, BookDescription
from rest_framework.serializers import ModelSerializer

class CategorySerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Category


class BookSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Book

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['category'] = CategorySerializer(instance.category).data
        return response

class BookDescriptionSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = BookDescription

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['book'] = BookSerializer(instance.book).data
        return response

