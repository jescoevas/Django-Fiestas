from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_parties),
    path('show/<int:id>', views.show_party),
    path('customer/<int:id>/parties', views.customer_parties),
    path('new/<int:id>/', views.new_party),
]