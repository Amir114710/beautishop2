from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class SocialMedia(models.Model):
    image = models.TextField(verbose_name='ادرس ایکون شبکه اجتماعی')
    link = models.TextField(verbose_name='لینک شبکه اجتماعی')
    color = models.TextField(verbose_name='رنگ شبکه اجتماعی')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.link
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'لینک شبکه های اجتماعی'
        verbose_name = 'لینک شبکه اجتماعی'

class Poster(models.Model):
    title = models.CharField(max_length=2500 , verbose_name='موضوع یا تیتر پوستر')
    content = RichTextUploadingField(null=True , blank=True , verbose_name='توضیحات بیشتر')
    image = models.ImageField(upload_to='home/images/' , verbose_name='تصویر پوستر')
    link = models.TextField(verbose_name='لینک موردنظر')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'پوستر ها'
        verbose_name = 'پوستر'

class Brand(models.Model):
    title = models.CharField(max_length=550 , verbose_name='نام برند')
    image = models.FileField(upload_to='home/images/' , verbose_name='تصویر برند')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'برند ها'
        verbose_name = 'برند'

class LittlePoster(models.Model):
    title = models.CharField(max_length=1500 , verbose_name='تیتر یا نام ویژگی')
    content = RichTextUploadingField(null=True , blank=True , verbose_name='توضیحات بیشتر')
    image = models.FileField(upload_to='home/images/' , verbose_name='تصویر مورد نظر برای این ویژگی')
    link = models.TextField(verbose_name='لینک مورد نظر')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'پوستر های تبلیفانی کوچکتر'
        verbose_name = 'پوستر'

class ShopAttr(models.Model):
    title = models.CharField(max_length=1500 , verbose_name='نام ویژگی')
    image = models.FileField(upload_to='home/images/' , verbose_name='تصویر')
    content = RichTextUploadingField(verbose_name='توضیحات')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'ویژگی های وبسایت'
        verbose_name = 'ویژگی وبسایت'

class Questions(models.Model):
    question = models.TextField(verbose_name='سوالات')
    answer = models.TextField(verbose_name='جواب سوال')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.question
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'سوالات متداول'
        verbose_name = 'سوال'

class CustomerClub(models.Model):
    phone = models.BigIntegerField(verbose_name='شماره تلفن' , null=True , blank=True)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.phone}'
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'باشگاه مشتریان'
        verbose_name = 'باشگاه مشتریان'

class Video(models.Model):
    video = models.FileField(upload_to='home/video/' , verbose_name = 'ویدیو')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'video'
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'ویدیو ها'
        verbose_name = 'ویدیو'

class Banner(models.Model):
    title = models.CharField(max_length=2500 , verbose_name='تیتر بنر')
    image = models.FileField(upload_to='home/banner/' , verbose_name='تصویر')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'بنر ها'
        verbose_name = 'بنر'

class Law(models.Model):
    content = RichTextUploadingField(verbose_name='توضیحات')

    def __str__(self):
        return f'توضیحات'
    
    class Meta:
        verbose_name_plural = 'قوانین'
        verbose_name = 'قانون'