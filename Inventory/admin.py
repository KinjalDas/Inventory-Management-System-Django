from django.contrib import admin

# Register your models here.

from .models import Item,Category,Client,Transaction

admin.site.register(Item)
admin.site.register(Client)
admin.site.register(Category)
admin.site.register(Transaction)
