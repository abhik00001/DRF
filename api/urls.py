from django.urls import path
from .views import *
urlpatterns = [
    path("companies",companies),
    path("companies/",search),
    path("companies/<int:id>",companies_data),
    path('register',register_view),
    path('login',login_view),
    path('logout',logout_view),
]
