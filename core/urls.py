from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from home.views import home_view
from users.views import profile_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", home_view, name="home"),
    path("profile/", include("users.urls")),
    path('@<username>/', profile_view, name='profile')
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
