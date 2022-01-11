from django.contrib import admin
from django.urls import path

from authentication.views import *




urlpatterns = [
    path('signup-user/', view=SignUpUserView.as_view(), name='signup-user'),
]