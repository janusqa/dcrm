from django.urls import path

from website import views


app_name = "website"

urlpatterns = [
    path("", views.home, name="home"),
    path("logout/", views.logout_user, name="logout"),
    path("register/", views.register_user, name="register"),
    path("records/<int:pk>/", views.record_detail, name="record"),
]
