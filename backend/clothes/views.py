from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()
from category.models import Category
from .models import Clothes
import json

# Create your views here.


class ClothesView(View):
    @staticmethod
    def clothes_to_dict(book):
        return {
            'id': book.id,
            'name': book.name,
            'slug': book.slug,
            'user': book.user.id,
            'category': book.category.id,
            'price': float(book.price),
            'quantity': book.quantity,
            'description': book.description,
            'created_at': book.created_at,
            'updated_at': book.updated_at,
            'brand': book.brand,
            'color': book.color,
            'size': book.size,
            'picture': str(book.picture),
        }

    def get(self, request, pk=None):
        if pk:
            try:
                book = Clothes.objects.get(pk=pk)
                return JsonResponse(self.clothes_to_dict(book))
            except Clothes.DoesNotExist:
                return HttpResponseBadRequest("Clothes not found.")
        else:
            clothes = Clothes.objects.all()
            data = [self.clothes_to_dict(book) for book in clothes]
            return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body) if request.body else {}
            user = User.objects.get(pk=data.pop('user'))
            category = Category.objects.get(pk=data.pop('category'))
            book = Clothes.objects.create(user=user, category=category, **data)
            return JsonResponse({"message": f"Clothes created successfully!"})
        except User.DoesNotExist:
            return HttpResponseBadRequest("User not found.")
        except Category.DoesNotExist:
            return HttpResponseBadRequest("Category not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error creating book: {str(e)}")

    def put(self, request, pk):
        try:
            book = Clothes.objects.get(pk=pk)
            data = json.loads(request.body) if request.body else {}
            if 'user' in data:
                book.user = User.objects.get(pk=data.pop('user'))
            if 'category' in data:
                book.category = Category.objects.get(pk=data.pop('category'))
            for key, value in data.items():
                setattr(book, key, value)
            book.save()
            return JsonResponse({"message": f"Clothes updated successfully!"})
        except Clothes.DoesNotExist:
            return HttpResponseBadRequest("Clothes not found.")
        except User.DoesNotExist:
            return HttpResponseBadRequest("User not found.")
        except Category.DoesNotExist:
            return HttpResponseBadRequest("Category not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error updating book: {str(e)}")

    def delete(self, request, pk):
        try:
            book = Clothes.objects.get(pk=pk)
            book.delete()
            return JsonResponse({"message": f"Clothes deleted successfully!"})
        except Clothes.DoesNotExist:
            return HttpResponseBadRequest("Clothes not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error deleting book: {str(e)}")
