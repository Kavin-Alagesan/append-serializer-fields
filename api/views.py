from rest_framework.views import APIView
from rest_framework import generics
from django.contrib.auth.models import User
from .serializer import UserSerializer,OfficialSerializer
from .models import OfficeModel
from rest_framework.response import Response

class CreateAPI(generics.ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        files = User.objects.all()
        dirs = OfficeModel.objects.all()

        context = {
            "request": request,
        }
        files_serializer = UserSerializer(files, many=True, context=context)
        dirs_serializer = OfficialSerializer(dirs, many=True, context=context)
        response = files_serializer.data + dirs_serializer.data

        return Response(response)