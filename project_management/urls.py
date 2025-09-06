from django.contrib import admin
from django.urls import path, include
from accounts.views import login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", login_view, name="root_login"),
    path('api/accounts/', include('accounts.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/tasks/', include('tasks.urls')),
]
