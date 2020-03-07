from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search_buildings),
    path('show/<int:id>/', views.show_building),
    path('owner/<int:userId>/buildings', views.owner_buildings),
    path('new/', views.new_building),
    path('admin/buildings',views.admin_buildings),
    path('admin/<int:id>/<str:choice>', views.admin_choice)
]