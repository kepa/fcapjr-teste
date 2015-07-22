from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, TemplateView
from .models import Banner, Mission, Vision, Value


class IndexView(TemplateView):
    template_name = 'index.html'

    def banners(self):
    	return Banner.objects.all()

    def mission(self):
    	mission = Mission.objects.all()
    	if mission.count() > 0:
    		return mission[0]

    def vision(self):
    	vision = Vision.objects.all()
    	if vision.count() > 0:
    		return vision[0]

    def values(self):
    	values = Value.objects.all()
    	if values.count() > 0:
    		return values[0]

    # def get_queryset(self):
    #     queryset = super(BannersView, self).get_queryset()
    #     return queryset


home = IndexView.as_view()
