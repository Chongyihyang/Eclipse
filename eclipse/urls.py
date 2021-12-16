from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from post.views import *
from registration.views import *
from django.urls import path, include # new

urlpatterns = [
    path('', home),
    path("create", addPost),            
    path('register', register),
    path('login', loginPage),
    path('login/', loginPage),
    path('post/<str:pk>', detail),
    path('logout', logoutPage),
    path('edit/<str:pk>', editpage),
    path('delete/<str:pk>', delete),
    path('del/<str:id>', deletecomment)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
