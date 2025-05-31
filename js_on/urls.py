from django.urls import path

from js_on.views import index

urlpatterns = [
    path('', index, name='index')
]