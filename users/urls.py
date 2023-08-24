from django.urls import path

from users.apps import UsersConfig
from users.services import generate_new_password
from users.views import LoginView, LogoutView, RegisterView, UserActivateView, UserProfileView, \
    UserForgotPasswordView, UserPasswordResetConfirmView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('activate/<str:uidb64>/<str:token>/', UserActivateView.as_view(), name='activate'),
    path('profile/', UserProfileView.as_view(), name='profile'),
    path('profile/genpassword/', generate_new_password, name='generate_new_password'),
    path('password_reset/', UserForgotPasswordView.as_view(), name='password_reset'),
    path('password_reset_confirm/<str:uidb64>/<str:token>/', UserPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
]