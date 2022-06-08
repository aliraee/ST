from django.urls import path
from .views import rest_method, test_method

urlpatterns = [
    path("test_url", test_method, name='my_method'),
    path("your_url", rest_method, name='default'),
]
