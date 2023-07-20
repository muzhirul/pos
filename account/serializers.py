from rest_framework import serializers
from account.models import *


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=68,min_length=6,write_only=True)
    # confirm_password = serializers.CharField(max_length=68,min_length=6,write_only=True)

    default_error_messages = {
        'username': 'The username should only contain alphanumeric characters'
    }
    class Meta:
        model = Account
        fields = ['id','email','password','username','first_name','last_name']
    
    def validate(self, attrs):
        username = attrs.get('username','')
        return attrs
    
    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)