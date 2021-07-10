from django.urls import path
from . import views

app_name ="entries"

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.entry, name="entry")
]
