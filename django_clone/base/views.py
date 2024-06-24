from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def greeting(request):
    return JsonResponse({'message': 'Hello, welcome to our API!'})