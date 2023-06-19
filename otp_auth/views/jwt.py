# Third-Party import
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Local import
from otp_auth.swagger import JWTResponseSerializer
from otp_auth.serializers import JWTObtainSerializer, JWTRefreshSerializer
from otp_auth.policies import JWTObtainAccessPolicy, JWTRefreshAccessPolicy
from otp_auth.signals import user_authenticated


class JWTObtainView(TokenObtainPairView):
    permission_classes = (JWTObtainAccessPolicy, )
    serializer_class = JWTObtainSerializer

    @swagger_auto_schema(responses={status.HTTP_201_CREATED: JWTResponseSerializer()})
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if status.is_success(response.status_code):
            user = request.user
            user_authenticated.send(sender=JWTObtainView, user=user, request=request)
        return response


class JWTRefreshView(TokenRefreshView):
    permission_classes = (JWTRefreshAccessPolicy, )
    serializer_class = JWTRefreshSerializer

    @swagger_auto_schema(responses={status.HTTP_201_CREATED: JWTResponseSerializer()})
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if status.is_success(response.status_code):
            user = request.user
            user_authenticated.send(sender=JWTRefreshView, user=user, request=request)
        return response
