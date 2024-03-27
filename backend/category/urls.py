from django.urls import path
from .views import CategoryView

urlpatterns = [
    path('', CategoryView.as_view(), name='category_list'),
    path('<int:pk>/', CategoryView.as_view(), name='category_detail'),
]

app_name = 'category'
