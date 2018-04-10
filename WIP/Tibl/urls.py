from django.urls import path
from django.views.generic.base import RedirectView

from . import views



urlpatterns = [
    path('<int:pk>', views.index, name='index'),
    path('', views.default_index, name='index'),
    path('classpage/<int:num_>', views.classpage, name='class'),
    path('messaging/<int:profile_id>', views.messaging, name='messages'),
    path('myprofile/<int:profile_id>', views.myprofile, name='myprofile'),
    path('friendprofile/<int:profile_id>', views.friendprofile, name='friendprofile'),
    path('classpage/<int:num_>/register', views.register_section_current, name='register_section_current'),
    path('classpage/<int:num_>/register_previous', views.register_section_previous, name='register_section_previous'),
]