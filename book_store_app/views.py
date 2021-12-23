from django.http import response
from rest_framework.generics import GenericAPIView, ListAPIView
from book_store_app.models import Category, Book, BookDescription
from book_store_app.serializers import BookSerializer, CategorySerializer, BookDescriptionSerializer
from rest_framework import response, status

# Category Api Endpoints 
class CategoryListView(ListAPIView):
    """GET - Get the list of Categories.."""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryCreateView(GenericAPIView):
    """POST- Create Category for books. Ex-Fiction, Non-fintion"""
    serializer_class = CategorySerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            slug = serializer.data.get('slug')
            # Check if the slug already exist
            category = Category.objects.filter(name=name, slug=slug)
            if category.exists():
                return response.Response({"error":"Category already exists."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                # Creating a new Category 
                new_cat = Category()
                new_cat.name = name
                new_cat.slug = slug
                new_cat.save()
                return response.Response({"succses":"Category created.."}, status=status.HTTP_201_CREATED)
        else:
            return response.Response({"error":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)
    
class CategoryUpdateView(GenericAPIView):
    """PUT- Update Category name and slug"""
    serializer_class = CategorySerializer
    def put(self, request, pk , format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Checking if the Category with pk exists
            category = Category.objects.filter(pk=pk)
            if category.exists():
                category = category[0]
                new_name = serializer.data.get('name')
                new_slug = serializer.data.get('slug')
                category.name = new_name
                category.slug = new_slug
                category.save()
                return response.Response({"success":"Category updated."}, status=status.HTTP_201_CREATED)
            else:
                return response.Response({"error":"Invalid id. No category exists."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({"error":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

class CategoryDeleteView(GenericAPIView):
    """DELETE- Delete Category of pk."""
    def delete(self,request, pk, format=None):
        category = Category.objects.filter(pk=pk)
        if len(category)>0:
            category = category[0]
            category.delete()
            return response.Response({"success":"Category deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return response.Response({"error":"Invalid Category."}, status=status.HTTP_400_BAD_REQUEST)

# Book Api Endpoints 
class BookListView(ListAPIView):
    """GET - Get the list of Books.."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(GenericAPIView):
    """POST- Create Books."""
    serializer_class = BookSerializer
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            cat = serializer.data.get('category')
            name = serializer.data.get('name')
            cash_price = serializer.data.get('cash_price')
            # Checking if the Category with pk exists
            category = Category.objects.filter(pk=cat)
            if category.exists():
                category = category[0]
                # Creating Book model
                book = Book()
                book.category = category
                book.name = name
                book.cash_price = cash_price
                book.save()
                return response.Response({"success":"Book created."}, status=status.HTTP_201_CREATED)
            else:
                return response.Response({"error":"Invalid category."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({"error":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

class BookUpdateView(GenericAPIView):
    """PUT- Update Books."""
    serializer_class = BookSerializer
    def put(self, request, pk , format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            # Checking if the Book with pk exists
            book = Book.objects.filter(pk=pk)
            if book.exists():
                book = book[0]
                cat = serializer.data.get('category')
                name = serializer.data.get('name')
                cash_price = serializer.data.get('cash_price')
                # Checking if the Category with pk exists
                category = Category.objects.filter(pk=cat)
                if category.exists():
                    category = category[0]
                    # Updating Book model
                    new_book = Book()
                    new_book.category = category
                    new_book.name = name
                    new_book.cash_price = cash_price
                    new_book.save()
                    return response.Response({"success":"Book updated."}, status=status.HTTP_201_CREATED)
                else:
                    return response.Response({"error":"Invalid category."}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return response.Response({"error":"Invalid book id."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return response.Response({"error":"Invalid data"}, status=status.HTTP_400_BAD_REQUEST)

class BookDeleteView(GenericAPIView):
    """DELETE- Delete Book of pk."""
    def delete(self,request, pk, format=None):
        book = Book.objects.filter(pk=pk)
        if len(book)>0:
            book = book[0]
            book.delete()
            return response.Response({"success":"Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return response.Response({"error":"Invalid Book."}, status=status.HTTP_400_BAD_REQUEST)



