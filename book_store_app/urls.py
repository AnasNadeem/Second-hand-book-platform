from django.urls import path
from book_store_app.views import (
    CategoryListView,
    CategoryCreateView, 
    CategoryUpdateView,
    CategoryDeleteView,
    )

urlpatters = [
    # Category- GET POST UPDATE DELETE
    path('list-cat/', CategoryListView.as_view()),
    path('create-cat/', CategoryCreateView.as_view()),
    path('update-cat/<int:pk>', CategoryUpdateView.as_view()),
    path('delete-cat/<int:pk>', CategoryDeleteView.as_view()),

]