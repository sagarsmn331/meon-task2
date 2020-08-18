from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import *
from newsapi import NewsApiClient
class UserViewSet(viewsets.ViewSet):
    def list(self,request):
        userlist=User.objects.all()
        data=[]
        for userlists in userlist:
            data.append({
                'id':userlists.id,
                'name':userlists.name,
                'state':userlists.state
            })
        return Response({'Data List':data})
    def create(self,request):
        usercreate=User()
        usercreate.id=request.data.get('id')
        usercreate.name=request.data.get('name')
        usercreate.state=request.data.get('state')
        usercreate.save()
        return Response({'Create data'})
