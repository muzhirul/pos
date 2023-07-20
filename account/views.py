from django.shortcuts import render
from rest_framework import generics, status
from account.serializers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response

# Create your views here.
class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        # serializer.is_valid(raise_exception=True)
        
        if serializer.is_valid(raise_exception=False):
            serializer.save()
            user_data = serializer.data
            user = Account.objects.get(username=user_data['username'])
            token= RefreshToken.for_user(user).access_token
            response = {
            "message": "New Customer Account Created Successfully",
            "error": False,
            "code": 201,
            "results": user_data
            }
            return Response(response, status=status.HTTP_201_CREATED)
        response = {
            "message": "Faild",
            "error": False,
            "code": 404
            }
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)
        # return Response(
        #         Msg.encode(201, "New Customer Account Created Successfully", None, user_data)
        #     , status=status.HTTP_201_CREATED)
