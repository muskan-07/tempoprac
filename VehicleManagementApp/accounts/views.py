from django.shortcuts import render
from rest_framework.views import APIView
from accounts.serializers import UserRegistrationSerializers,AdminUserRegistrationSerializers,UserLoginSerializer,VehicleDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from accounts.models import User,VehicleDetails
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
# Create your views here.
class UserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer=UserRegistrationSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            return Response({"Message":"User Registration Sucessful"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)


class AdminUserRegistrationView(APIView):
    def post(self,request,format=None):
        serializer=AdminUserRegistrationSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user=serializer.save()
            return Response({"Message":"Admin Registration sucessful"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class UserLoginView(APIView):
    def post(self,request,format=None):
        serializer=UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user=authenticate(email=email,password=password)
            if user is not None:
                token=get_tokens_for_user(user)
                return Response({'token':token,"msg":"login sucessfully"})
        return Response({"msg":"password not matched"},status=status.HTTP_400_BAD_REQUEST)


class AddVehicleview(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request,format=None):
        userid=request.user.id
        print(userid)
        user=User.objects.get(id=userid)
        print(user)
        
        if user.Is_superuser==True:
            serializer=VehicleDetailSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"Message":"VehicleDetails Added Sucessfully"},status=status.HTTP_201_CREATED)        
        return Response({"Message":"Only SuperUser has Acessto to Add vehicle Details"},status=status.HTTP_403_FORBIDDEN)

class VehicleUpdateView(APIView):
    permission_classes=[IsAuthenticated]
    def put(self,request,id,format=None):
        print(request)
        userid=request.user.id
        user=User.objects.get(id=userid)
        print(user)
        if user.Is_superuser==True or user.Is_admin == True:
            vehicledetails=VehicleDetails.objects.get(id=id)
            print(vehicledetails)
            serializer=VehicleDetailSerializer(vehicledetails,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({"Message":"updated Sucessfuly"},status=status.HTTP_202_ACCEPTED)                
        return Response({"Message":"only Admin and Superuser has Acess to it"},status=status.HTTP_403_FORBIDDEN)


    
    def delete(self,request,id,format=None):
        print(request)
        userid=request.user.id
        user=User.objects.get(id=userid)
        if user.Is_superuser==True:
            vehicledetails=VehicleDetails.objects.get(id=id)
            vehicledetails.delete()
            return Response({"Message":"Details deleted Sucessfully"})
        return Response({"Message":"only superuser has permission to delete"},status=status.HTTP_403_FORBIDDEN)

class AllVehicleDetailsview(APIView):
        permission_classes=[IsAuthenticated]
        def get(self,request,format=None):
            vehicledetails=VehicleDetails.objects.all()
            serializer=VehicleDetailSerializer(vehicledetails,many=True)
            return Response(serializer.data)
            







        





