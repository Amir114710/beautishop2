from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import View , TemplateView
from django.urls import reverse
from account.models import Address
from cart.cart_module import Cart
from shop.models import  Color, Product
from .cart_module import Cart
from .models import DiscountCode, Order, OrderItem
from mixins import AddressRequirdMixins, LoginRequirdMixins , LogoutRequirdMixins

class CartDetailView(TemplateView):
    template_name = 'includes/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context
    
class CartListDetailView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart'] = Cart(self.request)
        return context

class CartAddView(View):
    def post(self , request , slug):
        product = get_object_or_404(Product , slug = slug)
        quantity = request.POST.get('quantity')
        color = request.POST.get('color')
        value = request.POST.get('value')
        wieght = request.POST.get('wieght')
        cart = Cart(request)
        if int(quantity) > 0 and color is not None and value is not None:
            cart.add(product , quantity , color , wieght , value)
            return redirect(reverse('cart:cart_main_list'))
    
class CartDeleteView(View):
    def get(self , request , id):
        cart = Cart(request)
        cart.delete(id)
        return redirect(reverse('shop:shop_main'))
    
class OrderDetailView(AddressRequirdMixins , View):
    def get(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        return render(request , 'cart/checkout.html' , {'order':order})

class OrderCreationView(AddressRequirdMixins , View):
    def get(self , request):
        cart = Cart(request)
        order = Order.objects.create(user = request.user , total_price = cart.total() , post_price = cart.post_price())
        for item in cart:
            OrderItem.objects.create(order=order , product = item['product'] , quantity = item['quantity'] , color = item['color'] , value = item['value'] , price = item['price'] , post_price = item['post_price'])
        cart.remove_cart()
        return redirect('cart:order_detail' , order.id)
    
class ApplyDiscountView(AddressRequirdMixins , View):
    def post(self , request , pk):
        code = request.POST.get('discount_code')
        order = get_object_or_404(Order , id=pk)
        discount_code = get_object_or_404(DiscountCode , name=code)
        if discount_code.quantity == 0 :
            return redirect('cart:order_detail' , order.id)
        order.total_price -= order.total_price * discount_code.discount/100
        order.save()
        discount_code.quantity -= 1
        discount_code.save()
        return render(request , 'cart/checkout.html' , {'order':order , 'text':'تخفیف اعمال شد'})

class ApplyAddress(AddressRequirdMixins , View):
    def post(self , request , pk):
        order = get_object_or_404(Order , id=pk)
        address = request.POST.get('address')
        print(address)
        addresses = Address.objects.all()
        for x in addresses:
            if x.address == address:
                order.addresses = x
        for x in order.items.all():
            x.product.sale_count += 1
            x.product.inventory -= 1
            if x.product.inventory <= 0:
                x.product.statuc = False
            for a in x.product.color.all() :
                if a.title == x.color:
                    a.quantity -= 1
                    a.save()
            for y in x.product.value_product.all() :
                if y.title == x.value:
                    y.quantity -= 1
                    y.save()
            x.product.save()
        order.save()
        return redirect('pay:main_pay' , order.id)