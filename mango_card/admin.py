from django.contrib import admin
from .models import Mango, GenreMango, TypeMango, Comments

# Register your models here.

admin.site.register(Mango)
admin.site.register(GenreMango)
admin.site.register(TypeMango)
admin.site.register(Comments)