from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('membership', views.membership, name='membership'),
    path('blog', views.blog, name='blog'),
    path('blog-details', views.blogDetails, name='blogDetails'),
    path('contact', views.contact, name='contact')
]
