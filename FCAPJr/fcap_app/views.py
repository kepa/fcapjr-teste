from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView
from .models import Banner


class BannersView(ListView):
    model = Banner
    template_name = 'index.html'

    # def get_queryset(self):
    #     queryset = super(BannersView, self).get_queryset()
    #     return queryset


home = BannersView.as_view()
