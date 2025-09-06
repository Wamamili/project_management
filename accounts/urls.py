from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    profile_view, register_view, login_view, logout_view, dashboard_view,
    api_register, api_dashboard
)

urlpatterns = [
    # Template endpoints
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("dashboard/", dashboard_view, name="dashboard"),
    path("profile/", profile_view, name="profile"),

    # API endpoints
    path("api/register/", api_register, name="api_register"),
    path("api/dashboard/", api_dashboard, name="api_dashboard"),

    # JWT endpoints
    path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
