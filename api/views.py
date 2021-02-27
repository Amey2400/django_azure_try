from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import outputplotSerializer
from .models import outputplot
from rest_framework.response import Response
from django.http import HttpResponse
import sys
from subprocess import run,PIPE
from django.http import HttpResponse
sys.path.append("..")
from testserver import sample


class outputplotViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = outputplot.objects.all()
    serializer_class = outputplotSerializer

def senddata_topython(self):
  sample()
  return HttpResponse()
