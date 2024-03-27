from django.urls import path
from .views import ClothesView

urlpatterns = [
    path('', ClothesView.as_view(), name='clothes_list_create'),
    path('<int:pk>/', ClothesView.as_view(), name='clothes_detail_update_delete'),
]

app_name = 'clothes'
