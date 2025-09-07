from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (
    api_register,
    api_login,
    api_logout,
    api_dashboard,
    api_profile,
    api_change_password,
)

urlpatterns = [
    # Auth endpoints
    path("register/", api_register, name="api_register"),
    path("login/", api_login, name="api_login"),         
    path("logout/", api_logout, name="api_logout"),
    path("change-password/", api_change_password, name="api_change_password"),

    # User/profile endpoints
    path("dashboard/", api_dashboard, name="api_dashboard"),
    path("profile/", api_profile, name="api_profile"),

    # JWT endpoints (if you prefer token-based auth)
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
