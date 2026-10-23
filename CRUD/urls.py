
from django.urls import path
from CRUD.views import*

urlpatterns = [
    path('', insert, name='insert'),
    path('show', show, name='show'),
    path('edit', edit, name='edit'),
    path('delete', delete, name='delete')
]

