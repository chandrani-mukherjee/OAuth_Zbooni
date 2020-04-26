import datetime
import json
import pdb
import requests
import oauth2_provider
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from oauth.settings import AUTH_USER_MODEL
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.core.serializers import serialize
from .models import CustomUser
from .serializers import CreateUserSerializer
from rest_framework import permissions, routers, serializers, viewsets
from oauth2_provider.views.generic import ProtectedResourceView
from rest_framework import generics, permissions, serializers
from oauth2_provider.contrib.rest_framework import OAuth2Authentication,TokenHasReadWriteScope, TokenHasScope
from oauth2_provider.models import get_access_token_model, get_application_model
from oauth2_provider.settings import oauth2_settings
from django.contrib.auth.hashers import make_password

CLIENT_ID = 'Zbooni-1234'
CLIENT_SECRET = 'zbooni@12345'


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"email": "chandrani121189@gmail.com", "password": "1234abcd
	No bearere token required as User will be created intially 
    '''

    r = requests.post('http://localhost:8000/o/token/', 
            data={
                'grant_type': 'password',
                'username': request.data['email'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
    return Response(r.json())
   

@api_view(['GET'])
def UserList(request):
    '''
    Method to revoke tokens.
    Only Bearer Token required
	Return list of all Users and shows the validity of the tokens
    '''
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    AccessToken = get_access_token_model()
    all_users = CustomUser.objects.all()
    return_json = []
    for user_fetched in all_users:
        return_dict = {}
        return_dict['email'] = user_fetched.email
        
        user_with_token = AccessToken.objects.filter(user=user_fetched)
        for tk in user_with_token:
            print(user_with_token)
            print(user_with_token[0].__dict__)
            print(user_with_token[0].__dict__['expires'])
            print(user_with_token[0].__dict__['user_id' ])
            x = datetime.datetime.now().replace(tzinfo=None) >  user_with_token[0].__dict__['expires'].replace(tzinfo=None)
            print(" Expiry time ", x)
            return_dict['is_active'] = user_fetched.is_active
            try:
                return_dict['first_name'] = return_dict.first_name
                return_dict['last_name'] = return_dict.last_name
            except Exception as e:
               pass
            if x:
                return_dict['token_valid'] = False
            else:
                return_dict['token_valid'] = True
                break
            
        return_json.append(return_dict)
    return Response({"token":return_json})
    



@api_view(['POST'])
def activate(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"email": "chand@gmail.com"}
    '''
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    serializer_class = CreateUserSerializer
    custom_user_reference  =  CustomUser.objects.get(email=request.data["email"])
    custom_user_reference.is_active = True
    custom_user_reference.save()
    print(custom_user_reference)
    user_serializer = CreateUserSerializer(data=custom_user_reference.__dict__)
    
    
    if user_serializer.is_valid():
        print(user_serializer.validated_data)
       
    else:
          print(user_serializer.errors)
    return Response(user_serializer.data)



@api_view(['POST'])
def login(request):
    '''
    Registers user to the server. Input should be in the format:
    {"email": "chandrani121189@gmail.com", "password": "1234abcd"}
	Need Bearere Token
	Return success and token 
    '''
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    serializer_class = CreateUserSerializer
    print(request.data)
    password = make_password(request.data['password'])
    custom_user_model  = CustomUser(email=request.data['email'],password=password) 
    # Validate the data
    custom_user_model.is_staff = True
    custom_user_model.is_superuser = True
    custom_user_model.save()
    r = requests.post('http://localhost:8000/o/token/', 
            data={
                'grant_type': 'password',
                'username': request.data['email'],
                'password': request.data['password'],
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            },
        )
    return Response(r.json())


@api_view(['POST'])
def changePassword(request):
    '''
    Method to revoke tokens.
    {"email": "<email>","newpassword":"password"}
	Need Bearere Token
	Return sucess or not for password update
    '''
    authentication_classes = [OAuth2Authentication]
    permission_classes = [TokenHasScope]
    serializer_class = CreateUserSerializer
    custom_user_reference  =  CustomUser.objects.get(email=request.data["email"])
    password = make_password(request.data['newpassword'])
    custom_user_reference.password = password
    custom_user_reference.save()
    return Response({"passwordUpdated":"Success"})
    
    
