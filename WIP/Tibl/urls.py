from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('classpage/<int:num_>', views.classpage, name='class'),
    path('messaging/', views.messaging, name='messages'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('friendprofile/', views.friendprofile, name='friendprofile'),
]