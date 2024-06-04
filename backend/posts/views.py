from django.shortcuts import render
from django.contrib.auth import get_user_model
from .serializers import PostSerializer, UserSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly
from .models import Post 
# Create your views here.

class PostList(generics.ListCreateAPIView):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
    
class UserList(generics.ListCreateAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
