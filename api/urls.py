from django.urls import path
from api import views

urlpatterns = [
    path('api/',views.CreateAPI.as_view(),name='create'),
]
