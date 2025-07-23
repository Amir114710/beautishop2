from django.shortcuts import redirect, render
from django.views.generic import TemplateView , View , ListView

from blog.models import Article
from shop.models import Product, Timer
from .models import *

class HomeView(TemplateView):
    template_name = 'home/index.html'
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['posters'] = Poster.objects.all()[:1]
        context['brands'] = Brand.objects.all()
        context['little_posters'] = LittlePoster.objects.all()[:2]
        context['attrs'] = ShopAttr.objects.all()
        context['articles'] = Article.objects.filter(is_publish=True)[:3]
        context['questions'] = Questions.objects.all()
        context['special_product'] = Product.objects.filter(speacial=True)[:6]
        context['new_product'] = Product.objects.all()[:6]
        context['special_sale'] = Product.objects.filter(discount=True)[:6]
        context['video'] = Video.objects.all()[:1]
        context['banner'] = Banner.objects.all()[:1]
        return context
    
class FaqView(TemplateView):
    template_name = 'home/faq.html'

class CustomerClubView(View):
    def post(self , request):
        phone = request.POST.get('phone')
        CustomerClub.objects.create(phone=phone)
        return redirect('home:main')
    
class LawView(ListView):
    template_name = 'home/law.html'
    model = Law
    context_object_name = 'laws'