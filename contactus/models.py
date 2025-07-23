from django.db import models

class ContactInfo(models.Model):
    phone = models.CharField(max_length=550 , verbose_name='شماره تلفن' , null=True , blank=True)
    support = models.CharField(max_length=2500 , verbose_name='پشتیبانی مشتری' , help_text='شماره تلفن یا ایمیل')
    sell_support = models.CharField(max_length=2500 , verbose_name='پشتیبانی فروش' , help_text='شماره تلفن یا ایمیل')   
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.support
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'اطلاعات تماس'
        verbose_name = 'اطلاعات تماس'

class Contact(models.Model):
    name = models.CharField(max_length=2500 , verbose_name='نام')
    phone = models.BigIntegerField(default=0 , verbose_name='شماره تلفن')
    sub_title = models.CharField(max_length=3500 , verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('-created',)
        verbose_name_plural = 'تماس با ما'
        verbose_name = 'تماس با ما'
