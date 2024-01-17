from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('hello/', views.say_hello),
    path('storeJson/<str:id>/', views.store_json.as_view(), name='get_one'),
    path('storeJson/', views.store_json.as_view(), name='get_all/post'),


]