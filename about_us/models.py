from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class AboutUsMain(models.Model):
    title = models.CharField(max_length=2500 , verbose_name='تییتر توضیحات')
    content = RichTextUploadingField(verbose_name='توضیحات')
    image = models.FileField(upload_to='about/images/' , verbose_name='تصویر')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'توضیحات'
        verbose_name = 'توضیح'

class ConjuctionPoints(models.Model):   
    title = models.CharField(max_length=3500 , verbose_name='نام')
    year = models.BigIntegerField(default=0 , verbose_name='سال')
    content = RichTextUploadingField(verbose_name='توضیحات')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'نقاط عطف'
        verbose_name = 'نقطه عطف'