from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import  TemplateView , ListView , View , DetailView

from mixins import LogoutRequirdMixins
from shop.models import Favorite, Product , Category , Comment , CategoryParent
from django.http import FileResponse, Http404
from django.utils.encoding import iri_to_uri
import os
from django.conf import settings

class ShopView(ListView):
    template_name = 'shop/shop.html'
    model = Product
    context_object_name = 'products'
    paginate_by = 20
    def get_queryset(self):
        return Product.objects.filter(status=True)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.all()
        return context
    
class ProductDetail(View):
    template_name = 'shop/product_detail.html'
    def get(self , request , slug):
        product = get_object_or_404(Product , slug=slug)
        product.views +=1
        product.save()
        products = Product.objects.all()[:5]
        is_liked = None
        if request.user.is_authenticated:
            if self.request.user.user_favorite.filter(product__english_title = product.english_title , user_id = self.request.user.id).exists():
                is_liked = True
            else:
                is_liked = False
        return render(request , self.template_name , {'product':product , 'products':products , 'is_liked':is_liked})

# class ProductDetail(DetailView):
#     template_name = 'shop/product_detail.html'
#     model = Product
#     context_object_name = 'product'
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['products'] = Product.objects.all()[:5]
#         is_liked = None
#         if self.request.user.is_authenticated:
#             if self.request.user.user_favorite.filter(product__english_title = product.english_title , user_id = self.request.user.id).exists():
#                 context['is_liked'] = True
#             else:
#                 context['is_liked'] = False
#         return context
    
class CommentView(LogoutRequirdMixins , View):
    def post(self , request , slug):
        product = Product.objects.get(slug=slug)
        user = request.user
        message = request.POST.get('message')
        Comment.objects.create(user=user , product=product , message=message)
        return redirect('shop:product_detail' , slug)
    
def like(request , slug , pk):
    try:
        like = Favorite.objects.get(product__slug = slug , user_id=request.user.id)
        like.product.like_count -= 1
        like.product.save()
        like.delete()
    except:
        favorite = Favorite.objects.create(product_id=pk , user_id = request.user.id)
        favorite.product.like_count += 1
        favorite.product.save()
    return redirect('shop:product_detail' , slug)

class SearchBox(TemplateView):
    queryset = None
    template_name = "shop/shop.html"
    def get(self, request, *args, **kwargs):
        q = request.GET.get('q')
        queryset =  Product.objects.filter(title__icontains = q)
        return render(request , self.template_name , {'products':queryset})
    
class CategoryProductList(View):
    template_name = 'shop/shop.html'
    def get(self , request , id):
        category = get_object_or_404(Category , id=id)
        products = category.category_product.all()
        return render(request , self.template_name , {'products':products})
    
class CategoryParentProductList(View):
    template_name = 'shop/shop.html'
    def get(self , request , id):
        category = get_object_or_404(CategoryParent , id=id)
        products = category.parent_product.all()
        return render(request , self.template_name , {'products':products})
    
class FavoriteProductView(View):
    template_name = 'shop/shop.html'
    def get(self , request):
        products = Product.objects.filter(like_count__gt=5)
        return render(request , self.template_name , {'products':products})
    
class BigToMiniPriceProductView(View):
    template_name = 'shop/shop.html'
    def get(self , request):
        products = Product.objects.order_by('-price')
        return render(request , self.template_name , {'products':products})
    
class MiniToBigPriceProductView(View):
    template_name = 'shop/shop.html'
    def get(self , request):
        products = Product.objects.order_by('price')
        return render(request , self.template_name , {'products':products})
    