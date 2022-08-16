from django.urls import path
from . import views
urlpatterns = [
    path("", views.location, name="loc"),
    path("<str:p>", views.place, name="locations")]
