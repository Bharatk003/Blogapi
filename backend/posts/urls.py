from django.urls import path
from .views import PostList, PostDetail, UserList, UserDetail
from rest_framework.schemas import get_schema_view # new

urlpatterns = [
    path('users/', UserList.as_view()), # new
    path('users/<int:pk>/', UserDetail.as_view()),
    path('<int:pk>/', PostDetail.as_view()),
    path('', PostList.as_view()),
    path('openapi', get_schema_view( # new
        title="Blog API",
        description="A sample API for learning DRF",
        version="1.0.0"
), name='openapi-schema'),
    
]