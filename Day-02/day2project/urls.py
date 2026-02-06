
from django.contrib import admin
from django.urls import path,include
from . import app1

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include(app1.urls))
]
