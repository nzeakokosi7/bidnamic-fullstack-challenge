from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

urlpatterns = [
    path('/login', LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True),
         name='login'),
    path('/signup', LoginView.as_view(
        template_name='login.html',
        redirect_authenticated_user=True),
         name='sign-up'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
