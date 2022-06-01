from django.db import models

class Author(models.Model):
  name = models.CharField(max_length=255)
  surname = models.CharField(max_length=255)
  created_at = models.DateField(auto_now=True)

  def __str__(self):
    return self.name + " " + self.surname

class Book(models.Model):
  LANGUAGES = (
    ("FR", "Français"),
    ("EN", "English"),
    ("DE", "Deutsch")
  )
  
  author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=1000)
  language = models.CharField(choices=LANGUAGES, max_length=2)
  quantity = models.IntegerField(default=1)
  created_at = models.DateField(auto_now=True)

  def __str__(self):
    return self.title