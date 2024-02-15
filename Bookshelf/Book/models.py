# yourapp/models.py
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    Cat_name = models.CharField(max_length=255)
    def __str__(self):
        return self.Cat_name

class Author(models.Model):
    Author_id = models.IntegerField(primary_key=True)
    Authorname = models.TextField()
    def __str__(self):
        return self.Authorname

class Book(models.Model):
    isbn10 = models.CharField(max_length=255, unique=True)
    title = models.TextField()  
    authors = models.ForeignKey(Author, related_name='authors', on_delete=models.CASCADE) 
    categories = models.ForeignKey(Category, related_name='categories', on_delete=models.CASCADE) 
    thumbnail = models.URLField(blank=True)
    upload = models.ImageField(upload_to='uploads/', blank=True)
    description = models.TextField()
    published_year = models.IntegerField(null=True)
    average_rating = models.FloatField(null=True)
    num_pages = models.IntegerField(null=True)
    ratings_count = models.IntegerField(null=True, default=0)
    price = models.FloatField()
    publication_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def calculate_average_rating(self):
        # Calculate the average rating and update ratings_count for the book
        ratings_data = self.rated_products.aggregate(
            total_ratings=models.Avg('ratingno'),
            count=models.Count('ratingno')
        )
        total_ratings = ratings_data['total_ratings']
        count = ratings_data['count']

        self.average_rating = total_ratings if total_ratings is not None else 0
        self.ratings_count = count
        self.save()

class MyRating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, related_name='rated_products', on_delete=models.CASCADE)
    ratingno = models.IntegerField(default=1, validators=[MaxValueValidator(5), MinValueValidator(0)])

    def __str__(self):
        return f'Rated Book: {self.book}'

@receiver(post_save, sender=MyRating)
def update_average_rating(sender, instance, **kwargs):
    # Call the calculate_average_rating method after a MyRating instance is saved
    instance.book.calculate_average_rating()
