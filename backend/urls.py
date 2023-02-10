from django.urls import path
from .views import home,homeslug
urlpatterns = [
    path('',home),
    path('post/<slug:slug>/',homeslug)
]
