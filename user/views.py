from django.conf import settings
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
import json
import jwt
# Create your views here.


@api_view(['POST'])
def authenticate(request):
    serializer = UserSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(
            "Invalid Request"
        )
    try:
        user = User.objects.get(code=serializer.validated_data['code'])
        payload = {'user_id': user.id}

        bearer_token = jwt.encode(
            payload, settings.SECRET_KEY, algorithm='HS256')
        response = Response({'bearer_token': bearer_token})
        response.set_cookie("token", bearer_token)
        return response
    except User.DoesNotExist:
        return Response(False)
