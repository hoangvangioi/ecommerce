from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
from django.views import View


from .models import Book
from category.models import Category
import json

# Create your views here.


class BookView(View):
    @staticmethod
    def book_to_dict(book):
        return {
            'id': book.id,
            'name': book.name,
            'slug': book.slug,
            # 'user': book.user.id,
            'category': book.category.id,
            'price': str(book.price),
            'quantity': book.quantity,
            'description': book.description,
            'created_at': book.created_at,
            'updated_at': book.updated_at,
            'author': book.author,
            'picture': str(book.picture),
        }

    def get(self, request, pk=None):
        if pk:
            try:
                book = Book.objects.get(pk=pk)
                return JsonResponse(self.book_to_dict(book))
            except Book.DoesNotExist:
                return HttpResponseBadRequest("Book not found.")
        else:
            books = Book.objects.all()
            data = [self.book_to_dict(book) for book in books]
            return JsonResponse(data, safe=False)

    def post(self, request):
        try:
            data = json.loads(request.body) if request.body else {}
            # user = User.objects.get(pk=data.pop('user'))
            category = Category.objects.get(pk=data.pop('category'))
            book = Book.objects.create(category=category, **data)
            # book = Book.objects.create(user=user, category=category, **data)
            return JsonResponse({"message": f"Book created successfully!"})
        # except User.DoesNotExist:
        #     return HttpResponseBadRequest("User not found.")
        except Category.DoesNotExist:
            return HttpResponseBadRequest("Category not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error creating book: {str(e)}")

    def put(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            data = json.loads(request.body) if request.body else {}
            # if 'user' in data:
            #     book.user = User.objects.get(pk=data.pop('user'))
            if 'category' in data:
                book.category = Category.objects.get(pk=data.pop('category'))
            for key, value in data.items():
                setattr(book, key, value)
            book.save()
            return JsonResponse({"message": f"Book updated successfully!"})
        except Book.DoesNotExist:
            return HttpResponseBadRequest("Book not found.")
        # except User.DoesNotExist:
        #     return HttpResponseBadRequest("User not found.")
        except Category.DoesNotExist:
            return HttpResponseBadRequest("Category not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error updating book: {str(e)}")

    def delete(self, request, pk):
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            return JsonResponse({"message": f"Book deleted successfully!"})
        except Book.DoesNotExist:
            return HttpResponseBadRequest("Book not found.")
        except Exception as e:
            return HttpResponseBadRequest(f"Error deleting book: {str(e)}")
