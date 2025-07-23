from django.db import models
from django.urls import reverse
from account.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.text import slugify


class Tag(models.Model):
    title = models.CharField(max_length=2500 , null=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'تگ ها'
        verbose_name = 'تگ'
    
class Category(models.Model):
    title = models.CharField(max_length=2500 , null=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'دسته بندی ها'
        verbose_name = 'دسته بندی'
    
class Tip(models.Model):
    tip = models.TextField(null=True)
    
    def __str__(self):
        return self.tip

    class Meta:
        verbose_name_plural = 'نکته ها'
        verbose_name = 'نکته'
    
class Article(models.Model):
    author = models.ForeignKey(User , on_delete=models.CASCADE , related_name='articles',  verbose_name='نویسنده')
    category = models.ManyToManyField(Category , related_name='articles_cate' , verbose_name='دسته بندی')
    tag = models.ManyToManyField(Tag , related_name='article_tag' , verbose_name='تگ')
    tip = models.ManyToManyField(Tip , related_name='article_tip' , verbose_name='نکته' , null=True , blank=True)
    title = models.CharField(max_length=2500 , null=True , verbose_name='نام مقاله')
    slug = models.SlugField(null=True , blank=True)
    little_discription = RichTextUploadingField(verbose_name='توضیحات کوتاه')
    discription = RichTextUploadingField(verbose_name='توضیحات')
    image = models.FileField(upload_to='blog/image/' , verbose_name='تصویر')
    video = models.FileField(upload_to='blog/video/' , verbose_name='ویدیو' , null=True , blank=True)
    is_publish = models.BooleanField(default=True , verbose_name='نمایش داده شود')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article , self).save()
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'مقاله ها'
        verbose_name = 'مقاله'
    
    def get_absolute_url(self):
        return reverse('blog:article_detail', kwargs={'pk': self.pk})

class Comment(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='user_comment' , verbose_name='نویسنده')
    article = models.ForeignKey(Article , on_delete=models.CASCADE , related_name='art_comment' , verbose_name='مقاله')
    message = models.TextField(verbose_name='متن پیام')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.message
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'کامنت ها'
        verbose_name = 'کامنت '