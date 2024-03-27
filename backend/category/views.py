from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator
from django.views import View
from .models import Category
from django.views.generic import CreateView
import json

# Create your views here.


class CategoryView(View):
    @staticmethod
    def category_to_dict(category):
        return {
            'id': category.id,
            'name': category.name,
            'slug': category.slug,
        }

    # @method_decorator(login_required)
    def get(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(pk=pk)
                return JsonResponse(self.category_to_dict(category))
            except Category.DoesNotExist:
                return HttpResponseBadRequest("Category not found.")
        else:
            categories = Category.objects.all()
            data = [self.category_to_dict(category) for category in categories]
            return JsonResponse(data, safe=False)

    # @method_decorator(permission_required('category.add_category'))
    def post(self, request):
        try:
            # data = {key: request.data.get(key) for key in request.data}
            data = json.loads(request.body) if request.body else {}
            category = Category.objects.create(**data)
            return JsonResponse({"message": f"Category created successfully!"})
        except Exception as e:
            return HttpResponseBadRequest(f"Error creating category: {str(e)}")

    # @method_decorator(permission_required('category.change_category'))
    def put(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            # data = {key: request.data.get(key) for key in request.data}
            data = json.loads(request.body) if request.body else {}
            for key, value in data.items():
                setattr(category, key, value)
            category.save()
            return JsonResponse({"message": f"Category updated successfully!"})
        except Category.DoesNotExist:
            return HttpResponseBadRequest("Category not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error updating category: {str(e)}")

    # @method_decorator(permission_required('category.delete_category'))
    def delete(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            category.delete()
            return JsonResponse({"message": f"Category deleted successfully!"})
        except Category.DoesNotExist:
            return HttpResponseBadRequest("Category not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error deleting category: {str(e)}")
