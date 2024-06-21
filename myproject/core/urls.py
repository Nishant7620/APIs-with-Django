from django.urls import path
from core import views
urlpatterns = [
    path('get/',views.get,name='get'),
    path('post/',views.post,name ='post'),
    path('fetch_jokes/',views.fetch_jokes,name='fetch_jokes')
]
