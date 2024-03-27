from django.urls import path
from .views import MobileView

urlpatterns = [
    path('', MobileView.as_view(), name='mobile_list_create'),
    path('<int:pk>/', MobileView.as_view(), name='mobile_detail_update_delete'),
]

app_name = 'mobile'
