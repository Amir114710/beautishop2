from django.shortcuts import render
from django.views.generic import TemplateView
from .models import  AboutUsMain , ConjuctionPoints
from home.models import ShopAttr

class AboutUsView(TemplateView):
    template_name = 'about_us/about_us.html'    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_us'] = AboutUsMain.objects.all()[:1]
        context['attrs'] = ShopAttr.objects.all()
        context['points'] = ConjuctionPoints.objects.all()
        return context
    
