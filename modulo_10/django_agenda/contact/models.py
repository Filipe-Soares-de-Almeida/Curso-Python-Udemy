from django.db import models
from django.utils import timezone

# Create your models here.

# id (primary key)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), owner (foreign key)
# picture (image)


class Contact(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50, blank=True)
  phone = models.CharField(max_length=50)
  email = models.EmailField(max_length=254)
  created_date = models.DateTimeField(default= timezone.now)
  description = models.TextField(blank=True)
  # category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
  # show = models.BooleanField(default=True)
  # owner = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)
  # picture = models.ImageField(upload_to='pictures/%Y/%m/%d', blank=True, null=True)

  # def __str__(self):
  #   return f"{self.first_name} {self.last_name}"
