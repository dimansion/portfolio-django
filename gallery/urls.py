from django.conf.urls import url
from .views import photo_list

urlpatterns = [
    url(r'^$', photo_list, name='photo_list'),
] 