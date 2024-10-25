from django.urls import path
from feed import views

urlpatterns=[
    path('',views.loginView,name="loginPage"),
    path('home',views.homeView,name="homePage"),
    path('about',views.aboutView,name="aboutPage"),
    path('contact',views.contactView,name="contactPage"),
    path('posts',views.postsView,name="postsPage"),
    path('users',views.usersView,name="usersPage"),
    path('logout',views.logoutView,name="logoutV"),
]
