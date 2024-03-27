from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, HttpResponse
from django.db.models import Q
from itertools import chain
from book.models import Book
from clothes.models import Clothes
from mobile.models import Mobile

# Create your views here.


class SearchView(View):
    def get(self, request):
        query = request.GET.get("q")

        book = Book.objects.filter(name__contains=query).values()
        clothes = Clothes.objects.filter(name__contains=query).values()
        mobile = Mobile.objects.filter(name__contains=query).values()

        results = list(chain(book, clothes, mobile))
        return JsonResponse({"results": results})


