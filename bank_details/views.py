from django.shortcuts import render
from .models import BankDetails
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response


class BankIfsc(APIView):

    def get(self, request, format=None):
        obj = request.GET.get('ifsc')
        info = BankDetails.objects.filter(ifsc=obj).values()
        serializers = BankSerializers(info, many=True)
        return Response(serializers.data)


class BankName(APIView):

    def get(self, request, format=None):
        bank = request.GET.get('bank_name')
        city = request.GET.get('city')
        info1 = BankDetails.objects.filter(bank_name=bank, city=city).values()
        serializers = BankSerializers(info1, many=True)
        return Response(serializers.data)
