"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myApp import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('admin/', admin.site.urls),
    path('players/', views.show_player_info, name='players'),
    path('get-player-stats/<int:player_id>/', views.get_player_stats, name='get_player_stats'),
    path('games/', views.show_games, name='games'),
    path('game/<int:game_id>/delete/', views.game_delete, name='game_delete'),
    path('awards/', views.show_awards, name='awards'),
    path('add_award/', views.add_award, name='add_award'),
    path('get_awards/', views.get_awards, name='get_awards'),
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('validate_username/', views.validate_username, name='validate_username'),
    path('validate_email/', views.validate_email, name='validate_email')

]
