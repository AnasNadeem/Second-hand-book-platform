from django.urls import path
from book_store_app.views import (
    CategoryListView,
    CategoryCreateView, 
    CategoryUpdateView,
    CategoryDeleteView,
    BookListView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatters = [
    # Category- GET POST UPDATE DELETE
    path('list-cat/', CategoryListView.as_view()),
    path('create-cat/', CategoryCreateView.as_view()),
    path('update-cat/<int:pk>', CategoryUpdateView.as_view()),
    path('delete-cat/<int:pk>', CategoryDeleteView.as_view()),
    # Book- GET POST UPDATE DELETE
    path('list-book/', BookListView.as_view()),
    path('create-book/', BookCreateView.as_view()),
    path('update-book/<int:pk>', BookUpdateView.as_view()),
    path('delete-book/<int:pk>', BookDeleteView.as_view()),

]