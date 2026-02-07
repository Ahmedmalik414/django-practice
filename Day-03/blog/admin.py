from django.contrib import admin
from .models import Userprofile, Category, Tag, Blogpost

# Register models
admin.site.register(Userprofile)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Blogpost)
