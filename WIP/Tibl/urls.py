from django.urls import path, re_path
from . import views


urlpatterns = [
    path('<int:pk>', views.index, name='index'),
    path('classpage/<int:num_>', views.classpage, name='class'),
    path('messaging/<int:user_pk>/<int:friend_pk>', views.messaging, name='messages'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('friendprofile/', views.friendprofile, name='friendprofile'),
]