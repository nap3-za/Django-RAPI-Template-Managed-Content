from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

app_name="account"


urlpatterns = [
]

account_router = DefaultRouter()
account_router.register("app", views.AccountViewSet, basename="account")
urlpatterns += account_router.urls
