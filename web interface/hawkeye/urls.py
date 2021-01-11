from django.urls import path

from . import views
app_name = 'hawkeye'
urlpatterns = [
    path('', views.index, name='index'),
]