from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from django.views import generic

from .models import Boat


class IndexView(generic.ListView):
    context_object_name = 'boat_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Boat.objects.order_by('name')

