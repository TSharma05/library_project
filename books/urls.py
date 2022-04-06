from django.urls import path
from .views import *

app_name = 'books'

urlpatterns = [
    path('', book_list, name='book_list'),
    path('<int:book_id>/', book_view, name='book_view'),
    path('new/', book_create, name='book_new'),
    path('edit/<int:book_id>', book_update, name='book_edit'),
    path('delete/<int:book_id>', book_delete, name='book_delete')
]