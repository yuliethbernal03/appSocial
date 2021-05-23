from publicaciones.settings import MEDIA_ROOT
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', feed_view, name = 'feed_view'),
    path('profile/', profile_view, name = 'profile_view'),
    path('profile/<str:username>/', profile_view, name = 'profile_view'),
    path('register/', register_view, name = 'register_view'),
    path('login/', LoginView.as_view(template_name='login.html'), name = 'login_view'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name = 'logout_view'),
    path('post/', post_view, name = 'post_view'),
    path('follow/<str:username>/', follow_view, name = 'follow_view'),
    path('unfollow/<str:username>/', unfollow_view, name = 'unfollow_view'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)