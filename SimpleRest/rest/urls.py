from django.conf.urls import url
from .views import rest_method, test_method


urlpatterns = [
    url(r"test_url", test_method, name='my_method'),
    url(r"your_url", rest_method, name='default'),
]
