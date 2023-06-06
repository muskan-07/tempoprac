from rest_framework import serializers
from accounts.models import User,VehicleDetails

class UserRegistrationSerializers(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs ={'write_only':True}

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm password doesnot match")
        return attrs
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class AdminUserRegistrationSerializers(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model=User
        fields='__all__'
        extra_kwargs ={'write_only':True}

    def validate(self, attrs):
        password=attrs.get('password')
        password2=attrs.get('password2')
        if password != password2:
            raise serializers.ValidationError("password and confirm password doesnot match")
        return attrs
        
    def create(self, validated_data):
        return User.objects.create_adminuser(**validated_data)

class UserLoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=255)
    class Meta:
        model=User
        fields=['email','password']

class VehicleDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model=VehicleDetails
        fields=['VehicleNumber','VehicleType','VehicleModel','VehicleDescription']

