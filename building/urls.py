from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_buildings),
    path('show/<int:id>/', views.show_building)
]