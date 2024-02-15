from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book  # Adjust this import based on your actual model structure


def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})


from django.shortcuts import render
from .models import *

def new_arrival(request):
    

    arrival_books = Book.objects.order_by('-publication_date')[:10]  
    context = {'arrival_books': arrival_books}
    return render(request, 'arrival.html', context)

def featured_books(request):
    featured_books = Book.objects.all()[:7] 
    return render(request, 'featured_books.html', {'featured_books': featured_books})


def search_books(request):
    search_query = request.GET.get('search_query', '')
    found_books = Book.objects.filter(title__icontains=search_query)

    context = {'found_books': found_books, 'search_query': search_query}
    return render(request, 'search_results.html', context)


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'

  


