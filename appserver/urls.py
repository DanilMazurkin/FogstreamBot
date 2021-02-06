from django.urls import path
from .views import UserView

app_name = "appserver"
# app_name will help us do a reverse look-up latter.

urlpatterns = [
    path('create/user', UserView.as_view()),
]