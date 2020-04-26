from django.urls import path
from oauth.settings import AUTH_USER_MODEL
from . import views

urlpatterns = [
    path('register/', views.register),
    path('activate/', views.activate),
    path('login/', views.login),
    path('changePassword/', views.changePassword),
	path('UserList/',views.UserList)
]