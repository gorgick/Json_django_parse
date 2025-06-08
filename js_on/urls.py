from django.urls import path

from js_on.views import index, create_data

urlpatterns = [
    path('', index, name='index'),
    path('create_data', create_data, name='create_data')
]