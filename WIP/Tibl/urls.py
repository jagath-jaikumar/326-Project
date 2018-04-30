from django.urls import path
from django.views.generic.base import RedirectView

from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('classpage/<int:num_>', views.classpage, name='class'),
    path('messaging/', views.messaging, name='messages'),
    path('myprofile/', views.myprofile, name='myprofile'),
    path('friendprofile/<int:profile_id>', views.friendprofile, name='friendprofile'),
    path('register', views.register, name='register'),
    path('classpage/<int:num_>/register', views.register_section_current, name='register_section_current'),
 #   path('classpage/<int:num_>/register_previous', views.register_section_previous, name='register_section_previous'),
    path('class_search', views.class_search, name='class_search'),
]