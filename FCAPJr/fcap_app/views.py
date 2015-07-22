from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Banner, Mission, Vision, Value


class IndexView(TemplateView):
    template_name = 'index.html'

    def banners(self):
    	return Banner.objects.all()

    def mission(self):
    	return Mission.objects.all()[0]

    def vision(self):
    	return Vision.objects.all()[0]

    def values(self):
    	return Value.objects.all()[0]

    # def get_queryset(self):
    #     queryset = super(BannersView, self).get_queryset()
    #     return queryset


home = IndexView.as_view()
