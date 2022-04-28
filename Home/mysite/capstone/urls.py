from django.urls import include,path
from .import views

app_name="capstone"
urlpatterns = [
    path('', views.main, name='main'),

]
