from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('classpage/<int:num_>', views.classpage, name='class'),
    path('messaging/<int:profile_id>', views.messaging, name='messages'),
    path('myprofile/<int:profile_id>', views.myprofile, name='myprofile'),
    path('friendprofile/<int:profile_id>', views.friendprofile, name='friendprofile'),
]