from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('pyHealth/', include("pyHealth.urls")),
    path('admin/', admin.site.urls),
]
