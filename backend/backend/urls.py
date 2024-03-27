"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.http import JsonResponse, HttpResponse, QueryDict

def json_response(request):
    # data = {
    #     "message": "Hello World!",
        
    #     "book-list-and-create": "http://localhost:8000/book/",
    #     "book-detail-update-delete": "http://localhost:8000/book/<id>/",
        
    #     "category-list-and-create": "http://localhost:8000/category/",
    #     "category-detail-update-delete": "http://localhost:8000/category/<id>/",
        
    #     "clothes-list-and-create": "http://localhost:8000/clothes/",
    #     "clothes-detail-update-delete": "http://localhost:8000/clothes/<id>/",
        
    #     "mobile-list-and-create": "http://localhost:8000/mobile/",
    #     "mobile-detail-update-delete": "http://localhost:8000/mobile/<id>/",
       
    #     # "book-list-and-create": "http://localhost:8000/book/",
    #     # "book-detail-update-delete": "http://localhost:8000/book/<id>/",
    # }

    data = """
        <h2>Book</h2>

        <p>book-list-and-create</p>
        <a href="http://localhost:8000/book/">http://localhost:8000/book/</a>

        <p>book-detail-update-delete</p>
        <a href="http://localhost:8000/book/1/">http://localhost:8000/book/id/</a>

        <br>

        <h2>Category</h2>
        
        <p>category-list-and-create</p>
        <a href="http://localhost:8000/category/">http://localhost:8000/category/</a>

        <p>category-detail-update-delete</p>
        <a href="http://localhost:8000/category/1/">http://localhost:8000/category/id/</a>

        <br>

        <h2>Clothes</h2>
        
        <p>clothes-list-and-create</p>
        <a href="http://localhost:8000/clothes/">http://localhost:8000/clothes/</a>

        <p>clothes-detail-update-delete</p>
        <a href="http://localhost:8000/clothes/1/">http://localhost:8000/clothes/id/</a>

        <br>
        
        <h2>Mobile</h2>
        
        <p>mobile-list-and-create</p>
        <a href="http://localhost:8000/mobile/">http://localhost:8000/mobile/</a>

        <p>mobile-detail-update-delete</p>
        <a href="http://localhost:8000/mobile/1/">http://localhost:8000/mobile/id/</a>
    """
    return HttpResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),

    path("accounts/", include("django.contrib.auth.urls")),
    path('book/', include('book.urls', namespace='book')),
    path('clothes/', include('clothes.urls', namespace='clothes')),
    path('mobile/', include('mobile.urls', namespace='mobile')),
    path('category/', include('category.urls', namespace='category')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('search/', include('search.urls', namespace='search')),

    path("", json_response, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
