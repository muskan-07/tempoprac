from django.urls import path,include
from accounts.views import UserRegistrationView,AdminUserRegistrationView,UserLoginView,AddVehicleview,VehicleUpdateView,AllVehicleDetailsview
urlpatterns = [
    path('userregister/', UserRegistrationView.as_view(),name="userregister"),
    path('adminregister/', AdminUserRegistrationView.as_view(),name="adminregister"),
    path('login/', UserLoginView.as_view(),name="adminregister"),
    path('addvehicledetails/', AddVehicleview.as_view(),name="adminregister"),
    path('updatevehicledetails/<id>/',VehicleUpdateView.as_view(),name="adminregister"),
    path('allvehicledetails/',AllVehicleDetailsview.as_view(),name="adminregister"),
]