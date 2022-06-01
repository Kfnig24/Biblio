from django.shortcuts import render
from django.views import generic
from . import models

class IndexView(generic.ListView):
  template_name = "index.html"
  context_object_name = "books"

  def get_queryset(self): 
    return models.Book.objects.order_by('created_at')

class DetailView(generic.DetailView):
  model = models.Book
  template_name = 'detail.html'
  context_object_name = "book"