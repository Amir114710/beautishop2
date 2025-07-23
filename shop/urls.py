from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('' , ShopView.as_view() , name='shop_main'),
    path('detail/<str:slug>' , ProductDetail.as_view() , name='product_detail'),
    path('comment/<str:slug>' , CommentView.as_view() , name='comment'),
    path('like/<slug:slug>/<int:pk>' , like , name='like'),
    path('search/' , SearchBox.as_view() , name='search'),
    path('category_parent/<int:id>' , CategoryParentProductList.as_view() , name='category_parent'),
    path('category/<int:id>' , CategoryProductList.as_view() , name='category'),
    path('favorite_product' , FavoriteProductView.as_view() , name='faivor_product'),
    path('bigtomini' , BigToMiniPriceProductView.as_view() , name='bigtomini'),
    path('minitobig' , MiniToBigPriceProductView.as_view() , name='minitobig'),
]