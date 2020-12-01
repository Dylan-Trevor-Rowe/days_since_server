from django.core.exceptions import ValidationError
from django.http import HttpResponseServerError
from django.db.models import Count, Q
from dayssinceapi.models import WellBeing
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet