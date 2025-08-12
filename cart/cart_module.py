
from shop.models import Product


CART_SESSION_ID = 'cart'

class Cart:
    def __init__(self , request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart
    
    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            product = Product.objects.get(id = int(item['id']))
            item['product'] = product
            item['total'] = int(item['quantity']) * int(item['price'])
            item['unique_id'] = str(product.id)
            yield item

    def remove_cart(self):
        del self.session[CART_SESSION_ID]
        self.save()

    def add(self, product, quantity , color , wieght , value):
        product_id = str(product.id)
        wieght_total = int(wieght) * int(quantity)
        if wieght_total <= 1000 :
            post_total = 39000
        elif wieght_total > 1000:
            post_total = 78000
        if product_id not in self.cart or color != self.cart[product_id]['color'] or value != self.cart[product_id]['value'] :
            self.cart[product_id] = {'quantity': 0 , 'price': str(product.price) , 'post_price':post_total , 'wieght':wieght , 'color':color , 'value':value , 'id' : product.id}
        self.cart[product_id]['quantity'] += int(quantity)
        self.save()

    def total(self):
        cart = self.cart.values()
        for item in cart:
            wieght_total = int(item['wieght']) * int(item['quantity'])
            if wieght_total <= 1000 :
                post_total = 39000
            elif wieght_total > 1000:
                post_total = 78000
            total = int(item['price']) * int(item['quantity']) + post_total
        return total
    
    def post_price(self):
        cart = self.cart.values()
        post_price = sum(int(item['post_price']) * int(item['quantity']) for item in cart)
        return post_price
    
    def wieght(self):
        cart = self.cart.values()
        post_price = sum(int(item['wieght']) * int(item['quantity']) for item in cart)
        return post_price

    def delete(self , id):
        if id in self.cart:
            del self.cart[id]
            self.save()

    def save(self):
        self.session.modified = True