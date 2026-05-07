from django.urls import path
from django.contrib.auth import views as auth_views  # <--- Add this line!
from .views import SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("login/", auth_views.LoginView.as_view(extra_context={'is_auth_page': True}), name="login"),
    w
]