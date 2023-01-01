import genericpath
from django.shortcuts import render
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework import status
from .import serialzers


class ProfileView(genericpath.RetrieveAPIView):
    serializer_class = serialzers.UserSerializer

    def get_object(self):
        return self.request.user


class LoginView(views.APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializer.LoginSerializer(data=self.request.data,
                                                context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)
