from http import HTTPStatus

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from todos import models
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = models.Todo.objects.all()
    serializer_class = TodoSerializer


class HealthCheckView(APIView):
    def get(self, request):
        return Response(status=HTTPStatus.OK)