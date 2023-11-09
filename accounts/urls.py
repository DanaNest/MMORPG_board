from . import views
from django.urls import path


from accounts.forms import register

urlpatterns = [
    path('register/', register, name='register'),

]