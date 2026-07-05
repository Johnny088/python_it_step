from django.contrib.auth.views import LogoutView
from django.urls import path

from main.views import index_view, SignUpView, CustomSignInView

urlpatterns = [
    path('', index_view, name='index'),
    path('sign-in/', CustomSignInView.as_view(), name='sign-in'),
    path('sign-up/', SignUpView.as_view(), name='sign-up'),
    path('logout/', LogoutView.as_view(), name='logout'),

]