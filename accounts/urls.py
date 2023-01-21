from django.urls import path
from .views import (
    SignUpView, LoginView, LogoutView, UpdatePasswordViewSet, ProfileViewSet
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

PUT = {"put": "update"}
RETRIEVE_UPDATE = {
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update'
}

urlpatterns = [
    path('signup/', SignUpView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('update_password/', UpdatePasswordViewSet.as_view(PUT)),
    path('profile/', ProfileViewSet.as_view(RETRIEVE_UPDATE)),

    path('api/jwt_token/create', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/jwt_token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/jwt_token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
