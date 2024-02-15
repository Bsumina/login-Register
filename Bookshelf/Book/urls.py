
# yourapp/urls.py
from django.urls import path
from .views import BookDetailView
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('featured/', featured_books, name='featured_books'),
    path('search/', search_books, name='search_books'),
    path('book/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('new_arrival/', new_arrival, name='new_arrival'),
    # Add other URLs as needed
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)