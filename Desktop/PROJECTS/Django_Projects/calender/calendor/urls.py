from django.urls import path
from . import views

urlpatterns = [
    path("api/<int:year>/", views.api_calendar, name="api_calendar"),
    path("calendar", views.year_calendar,name="calendar"),

]
