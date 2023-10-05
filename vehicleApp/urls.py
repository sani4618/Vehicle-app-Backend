from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.RegVehicle,name="register"),
    path('viewall/',views.viewVehicleDetails,name="view"),
    path('search/',views.SearchVehicleDetails,name="search"),
    path('delete/',views.DeleteVehicleDetails,name="delete")
   
]