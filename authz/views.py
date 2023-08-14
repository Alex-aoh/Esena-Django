from django.shortcuts import render
from django.http import HttpResponse
from .auth0.auth0_management_token import requestToken, askNewToken
# Create your views here.

def requestTokenView(request): 
    return HttpResponse(requestToken())