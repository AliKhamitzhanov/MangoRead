from django.urls import path
from .views import MangoViewSet, MangoCommentsViewSet, CommentsViewSet

LIST = {'get': 'list'}
RETRIEVE = {'get': 'retrieve'}
RETRIEVE_CREATE = {'get': 'retrieve', 'post': 'create'}

urlpatterns = [
    path('mango/', MangoViewSet.as_view(LIST), name='mango'),
    path('mango/<int:pk>/', MangoViewSet.as_view(RETRIEVE), name='mango_detail'),

    path('mango/<int:pk>/comments/', MangoCommentsViewSet.as_view(RETRIEVE_CREATE), name='mango_comments'),
    path('comments/<int:pk>/', CommentsViewSet.as_view(), name='comments'),
]
