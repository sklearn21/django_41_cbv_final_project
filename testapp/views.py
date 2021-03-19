from django.shortcuts import render
from testapp.models import Beer
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.

class BeerListView(ListView):
    model = Beer
    # default template file testapp/beer_list.html


class BeerDetailView(DetailView):
    model = Beer


class BeerCreateView(CreateView):
    model = Beer
    fields='__all__'


class BeerUpdateView(UpdateView):
    model = Beer
    fields = ('taste', 'color', 'price')


class BeerDeleteView(DeleteView):
    model = Beer
    success_url = reverse_lazy('home')