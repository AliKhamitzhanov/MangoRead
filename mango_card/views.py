from .models import Mango, Comments
from .serializer import MangoListSerializer, MangoDetailSerializer, MangoCommentsSerializer, CommentCreateSerializer, CommentsSerializer
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets, generics, permissions, mixins
from accounts.permissions import IsOwnerOrReadOnly


class MangoViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """ViewSet for viewing Book model instances."""
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Mango.objects.all()
    serializer_class = MangoListSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['genre', 'type', 'released']
    search_fields = ['title']

    def get_serializer_class(self):
        if self.action == "list":
            return MangoListSerializer
        return MangoDetailSerializer


class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('title_only'):
            return ['title']
        return super().get_search_fields(view, request)


class MangoCommentsViewSet(viewsets.ModelViewSet):
    """Viewing and adding comments for a specific Book model instance."""
    queryset = Mango.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        return MangoCommentsSerializer if self.request.method in permissions.SAFE_METHODS else CommentCreateSerializer

    def perform_create(self, serializer):
        serializer.validated_data['book'] = Mango.objects.get(pk=self.kwargs['pk'])
        serializer.save()


class CommentsViewSet(generics.RetrieveUpdateDestroyAPIView):
    """View and edit one comment."""
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = [IsOwnerOrReadOnly]