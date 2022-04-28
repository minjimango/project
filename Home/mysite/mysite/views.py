from django.contrib import admin
from django.urls import path
import capstone.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', capstone.views.main, name='main'),

]
