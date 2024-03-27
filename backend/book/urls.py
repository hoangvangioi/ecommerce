from django.urls import path
from .views import BookView

urlpatterns = [
    path('', BookView.as_view(), name='book_list_create'),
    path('<int:pk>/', BookView.as_view(), name='book_detail_update_delete'),
]

app_name = 'book'
