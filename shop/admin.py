from django.contrib import admin
from .models import *

admin.site.register(CategoryParent)
admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Value)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Favorite)
admin.site.register(Timer)