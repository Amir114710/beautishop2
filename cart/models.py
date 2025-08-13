from django.db import models
from account.models import Address, User
from datetime import datetime
from shop.models import Product

class Order(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='orders' , verbose_name='کاربر')
    total_price = models.IntegerField(default=0, verbose_name='قیمت کلی')
    post_price = models.IntegerField(default=0, verbose_name='هزینه پست')
    created_at = models.DateTimeField(auto_now_add=True)
    is_pay = models.BooleanField(default=False , verbose_name='ایا پرداخت شده است ؟')
    addresses = models.ForeignKey(Address , on_delete = models.CASCADE , related_name='order_address' , blank=True , null=True, verbose_name='آدرس کاربر')
    image_payed = models.FileField(upload_to='pay/image', null=True , blank=True , verbose_name='عکس پرداخت موفق')
    DeliveryDate = models.DateTimeField(null=True , blank=True , verbose_name='تاریخ تحویل محصول')
    status = models.BooleanField(default=False , verbose_name='وضعیت')

    def __str__(self) -> str:
        return self.user.phone
    
    class Meta:
        ordering = ("-created_at",)
        verbose_name = "ثبت درخواست خرید"
        verbose_name_plural = "تنظیمات قسمت ثبت درخواست خرید ها"

class OrderItem(models.Model):
    order = models.ForeignKey(Order , on_delete=models.CASCADE , related_name='items' , verbose_name='کالا درحال انجام')
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='items' , verbose_name='کالا')
    quantity = models.SmallIntegerField(verbose_name='تعداد')
    color = models.CharField(max_length=550 , verbose_name='رنگ' , null=True , blank=True)
    value = models.CharField(max_length=550 , verbose_name='حجم' , null=True , blank=True)
    size = models.CharField(max_length=550 , verbose_name='سایز' , null=True , blank=True)
    price = models.PositiveIntegerField(verbose_name='قیمت')
    post_price = models.BigIntegerField(default=0 , verbose_name='هزینه پست' , null=True , blank=True)

    def __str__(self) -> str:
        return self.order.user.phone
    
    class Meta:
        verbose_name = "پایان ثبت درخواست خرید"
        verbose_name_plural = "تنظیمات قسمت  پایان ثبت درخواست خرید ها"


class DiscountCode(models.Model):
    name = models.CharField(max_length=100 , verbose_name='نام کد تخفیف' , unique=True)
    discount = models.SmallIntegerField(default=0 , verbose_name='مقدار درصد تفیف')
    quantity = models.SmallIntegerField(default=1 , verbose_name='تعداد کد تخفیف')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "کد تخفیف"
        verbose_name_plural = "تنظیمات قسمت  کد های تخفیف"



