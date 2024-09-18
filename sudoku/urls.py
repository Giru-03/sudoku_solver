from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_sudoku, name='upload_sudoku'),
]
