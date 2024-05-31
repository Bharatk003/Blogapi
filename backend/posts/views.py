from django.shortcuts import render
from .serializers import PostSerializer
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
