from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse
from django.utils.text import slugify
from account.models import User

class CategoryParent(models.Model):
    title = models.CharField(max_length=1500 , verbose_name='نام سر دسته')
    image = models.FileField(upload_to='shop/images/' , verbose_name='تصویر')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'سر دسته ها'
        verbose_name = 'سر دسته'

class Category(models.Model):
    parent = models.ForeignKey(CategoryParent , on_delete=models.CASCADE , related_name='category_parent' , verbose_name='سر دسته')
    title = models.CharField(max_length=1500 , verbose_name='نام دسته بندی')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'دسته بندی ها'
        verbose_name = 'دسته بندی'

class Color(models.Model):
    title = models.CharField(max_length=550 , verbose_name='نام اصلی' , null=True , blank=True)
    color = models.CharField(max_length=550 , verbose_name='رنگ')
    quantity = models.IntegerField(default=0 , verbose_name='تعداد')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'رنگ ها'
        verbose_name = 'رنگ'

class Value(models.Model):
    title = models.CharField(max_length=550 , verbose_name='نام اصلی' , null=True , blank=True)
    value = models.CharField(max_length=550 , verbose_name='حجم')
    quantity = models.IntegerField(default=0 , verbose_name='تعداد')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.value
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'حجم ها'
        verbose_name = 'حجم'

class Product(models.Model):
    title = models.CharField(max_length=1500 , verbose_name='نام کالا')
    english_title = models.CharField(max_length=1500 , verbose_name='نام انگلیسی کالا')
    slug = models.SlugField(null=True , blank=True)
    category = models.ManyToManyField(Category , related_name='category_product' , verbose_name='دسته بندی')
    category_parent = models.ForeignKey(CategoryParent , on_delete=models.CASCADE , related_name='parent_product' , verbose_name='سر دسته' , null=True , blank=True)
    color = models.ManyToManyField(Color , related_name='product_color' , verbose_name='رنگ ها' , null=True , blank=True)
    value_product = models.ManyToManyField(Value , related_name='product_value' , verbose_name='حجم ها' , null=True , blank=True)
    price = models.BigIntegerField(default=0 , verbose_name='قیمت کالا به تومان')
    post_price = models.BigIntegerField(default=0 , verbose_name='قیمت پست کالا به تومان' , null=True , blank=True)
    discount_percent = models.BigIntegerField(default=0 , null=True , blank=True , verbose_name='درصد تخفیف')
    discount_test = models.BigIntegerField(default=0 , blank=True , verbose_name='درصد تخفیف' , help_text='لطفا تکرار شود')
    new_price = models.BigIntegerField(null=True , blank=True , verbose_name='قیمت تخفیف خورده' , help_text='(این فیلد نیاز به پر شدن ندارد)')
    little_content = RichTextUploadingField(verbose_name='توضیحات کوتاه')
    content = RichTextUploadingField(verbose_name='توضیحات کامل')
    ingredients = RichTextUploadingField(verbose_name='مواد تشکیل دهنده')
    how_to_use = RichTextUploadingField(verbose_name='نحوه استفاده')
    image1 = models.FileField(upload_to='shop/images/' , verbose_name='تصویر کالا' , null=True , blank=True)
    image2 = models.FileField(upload_to='shop/images/' , verbose_name='تصویر کالا' , null=True , blank=True)
    image3 = models.FileField(upload_to='shop/images/' , verbose_name='تصویر کالا' , null=True , blank=True)
    image4 = models.FileField(upload_to='shop/images/' , verbose_name='تصویر کالا' , null=True , blank=True)
    image5 = models.FileField(upload_to='shop/images/' , verbose_name='تصویر کالا' , null=True , blank=True)
    image6 = models.FileField(upload_to='shop/images/' , verbose_name='تصویر کالا' , null=True , blank=True)
    value = models.CharField(max_length=550 , verbose_name='اندازه')
    wieght = models.BigIntegerField(default=0 , verbose_name='وزن' , help_text='گرم')
    inventory = models.BigIntegerField(default=0 , verbose_name='موجودی')
    inventory_view = models.BigIntegerField(default=0 , verbose_name='موجودی برای نمایش')
    views = models.BigIntegerField(default=0 , verbose_name='بازدید ها')
    status = models.BooleanField(default=True , verbose_name='موجودی')
    sale_count = models.BigIntegerField(default=0 , verbose_name='تعداد فروش رفته' , help_text='نیاز به پر کردن این بهش نیست')
    speacial = models.BooleanField(default=True , verbose_name='محصول خاص')
    discount = models.BooleanField(default=False , verbose_name='تخفیف')
    like_count = models.BigIntegerField(default=0 , verbose_name='تعداد لایک ها')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'کالاها'
        verbose_name = 'کالا'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.english_title)
        new = self.price * self.discount_percent/100
        self.price = self.price - new
        self.discount_percent = 0
        super(Product , self).save()

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'slug': self.slug})
    
class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_comments' , verbose_name='کاربر')
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='product_comment' , verbose_name='کالا')
    message = models.TextField(verbose_name='پیام')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'نظرها'
        verbose_name = 'نظر'

class Favorite(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_favorite' , verbose_name='کاربر')
    product = models.ForeignKey(Product , on_delete=models.CASCADE , related_name='product_favorite' , verbose_name='کالا')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'علاقه مندی ها'
        verbose_name = 'علاقه'

class Timer(models.Model):
    timer = models.TimeField(null=True , blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'timer'
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'زمان شمار برای محصولات ویژه'
        verbose_name = 'زمان شمار برای محصولات ویژه'
