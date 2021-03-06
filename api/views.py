from django.shortcuts import render

# Create your views here.

from .models import *
from .serializers import *
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class EventList(APIView):
    """
    List all Events, or create a new Event
    """
    def get(self,request, format=None):
        event=Event.objects.all()
        serializer=EventSerializer(event,many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer=EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class EventDetail(APIView):
#     """
#     Retrieve, update or delete a Event instance
#     """
#     def get_object(self,pk):
#         try:
#             return Event.objects.get(pk=pk)
#         except Event.DoesNotExist:
#             raise Http404

#     def get(self, request,pk, format=None):
#         Event=self.get_object(pk)
#         serializer=EventSerializer(Event)
#         return Response(serializer.data)
    
#     def put(self, request, pk, format=None):
#         Event=self.get_object(pk)
#         serializer = EventSerializer(Event, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk,format=None):
#         Event = self.get_object(pk)
#         Event.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class BlogList(APIView):
    """
    List all Events, or create a new Event
    """
    def get(self,request, format=None):
        event=Blog.objects.all()
        serializer=BlogSerializer(event,many=True)
        print("blog serializer data",serializer.data)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer=BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



# GameRecord ApiView

class GameRecordList(APIView):
    """
    List all Events, or create a new Event
    """
    def get(self,request, format=None):
        games=GameRecord.objects.all()
        # print("gamessssssssssssssssssssss",games)

        serializer=GameRecordSerializer(games, many=True)
        print("serializersssssssssssss",serializer)
        print("dataaaaaaaaaaaaaaaaaaaaa",serializer.data)

        return Response(serializer.data)
    def post(self, request, format=None):
        serializer=GameRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
