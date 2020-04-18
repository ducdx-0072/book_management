from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework import exceptions
from rest_framework.status import {
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK,
    HTTP_500_INTERNAL_SERVER_ERROR
}
from rest_framework.response import Response
from .models import BookUser


"""Function Login

Raises:
    exceptions.AuthenticationFailed: if password is wrong

Returns:
    [User] -- [User information]
"""

@csrf_exempt
@api_view(["POST"])
@authentication_classes([])
@permission_classes([AllowAny, ])
def login(request, version):
    email = request.data.get("email")
    password = request.data.get("password")
    response = {}
    status = HTTP_200_OK
    if email is None or password is None:
        response["status"] = -1
        response["message"] = "Email or password is invalid"
        return Response(response, status=HTTP_400_BAD_REQUEST)

    # Check email exist or not
    try:
        user = BookUser.objects.get(email=email)
    except User.DoesNotExist:
        raise exceptions.AuthenticationFailed("No such user")

    # In case of email exist, check password
    if user.check_password(password):
        token, _ = Token.objects.get_or_create(user=user)
        esponse["status"] = 1
        response["message"] = "Login successful"
        response['user_id'] = user.id
        response['user_name'] = user.username
        response['email'] = user.email
        response["token"] = token.key
        status = HTTP_200_OK
    else:
        response["status"] = -1
        response["message"] = "Invalid Credentials"
        status = HTTP_404_NOT_FOUND

    return Response(response, status=status)


"""
Function Logout
"""
@csrf_exempt
@api_view(["GET"])
def logout(request, version):
    request.user.auth_token.delete()
    return Response(status=HTTP_200_OK)
