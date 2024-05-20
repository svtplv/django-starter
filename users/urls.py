from django.urls import path

from .views import (
    profile_emailchange,
    profile_settings_view,
    profile_view,
    profile_edit_view,
)


urlpatterns = [
    path("", profile_view, name="profile"),
    path("edit/", profile_edit_view, name="profile-edit"),
    path("onboarding/", profile_edit_view, name="profile-onboarding"),
    path("settings/", profile_settings_view, name="profile-settings"),
    path("emailchange/", profile_emailchange, name="profile-emailchange"),
]
