from rest_framework import serializers
from . import models
from django.contrib.auth.models import User

class ClientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Client
        fields = '__all__' 

class RegistratonSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required = True)
    mobile_no = serializers.CharField(max_length=12)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'mobile_no', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        email = self.validated_data['email']
        mobile_no = self.validated_data['mobile_no']
        password= self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error':'Password did not match'})
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        
        account = User(username = username, email = email)
        account.set_password(password)
        account.is_active = False
        account.save()

        models.Client.objects.create(
            user=account,
            mobile_no=mobile_no,
            role='customer'
        )

        return account
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)