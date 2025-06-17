from rest_framework.views import APIView # making class as a API
from django.http import JsonResponse # seding response
from .Serializer import *
from .models import *


class userSignup(APIView):
    def post(self,request):
        serializersData=userDetailsSerializer(data=request.data)
        if serializersData.is_valid():
            usersDetails.objects.create(**serializersData.data)
            message = {"message":"User signedup successfully"}
            return JsonResponse(message)
        return JsonResponse(serializersData.errors)


class userMembership(APIView):
    def get(self,request,email):
         result =list((membershipDetails.objects.filter(email=email).values()))
         message ={"membership Details":result}
         return JsonResponse(message)