from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View
from django.contrib.auth import get_user_model
from django.conf import settings


User = get_user_model()
from category.models import Category
from .models import Mobile
import json

# Create your views here.


class MobileView(View):
    @staticmethod
    def mobile_to_dict(mobile):
        return {
            'id': mobile.id,
            'name': mobile.name,
            'slug': mobile.slug,
            'user': mobile.user.id,
            'category': mobile.category.id,
            'price': float(mobile.price),
            'quantity': mobile.quantity,
            'description': mobile.description,
            'created_at': mobile.created_at,
            'updated_at': mobile.updated_at,
            'brand': mobile.brand,
            'picture': str(mobile.picture),
        }

    def get(self, request, pk=None):
        if pk:
            try:
                mobile = Mobile.objects.get(pk=pk)
                return JsonResponse(self.mobile_to_dict(mobile))
            except Mobile.DoesNotExist:
                return HttpResponseBadRequest("Mobile not found.")
        else:
            mobiles = Mobile.objects.all()
            data = [self.mobile_to_dict(mobile) for mobile in mobiles]
            return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            # data = {key: request.POST.get(key) for key in request.POST}
            data = json.loads(request.body) if request.body else {}
            user = User.objects.get(pk=data.pop('user'))
            category = Category.objects.get(pk=data.pop('category'))
            mobile = Mobile.objects.create(user=user, category=category, **data)
            return JsonResponse({"message": f"Mobile created successfully!"})
        except User.DoesNotExist:
            return HttpResponseBadRequest("User not found.")
        except Category.DoesNotExist:
            return HttpResponseBadRequest("Category not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error creating mobile: {str(e)}")

    def put(self, request, pk):
        try:
            mobile = Mobile.objects.get(pk=pk)
            # data = {key: request.POST.get(key) for key in request.POST}
            data = json.loads(request.body) if request.body else {}
            if 'user' in data:
                mobile.user = User.objects.get(pk=data.pop('user'))
            if 'category' in data:
                mobile.category = Category.objects.get(pk=data.pop('category'))
            for key, value in data.items():
                setattr(mobile, key, value)
            mobile.save()
            return JsonResponse({"message": f"Mobile updated successfully!"})
        except Mobile.DoesNotExist:
            return HttpResponseBadRequest("Mobile not found.")
        except User.DoesNotExist:
            return HttpResponseBadRequest("User not found.")
        except Category.DoesNotExist:
            return HttpResponseBadRequest("Category not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error updating mobile: {str(e)}")

    def delete(self, request, pk):
        try:
            mobile = Mobile.objects.get(pk=pk)
            mobile.delete()
            return JsonResponse({"message": f"Mobile deleted successfully!"})
        except Mobile.DoesNotExist:
            return HttpResponseBadRequest("Mobile not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error deleting mobile: {str(e)}")
