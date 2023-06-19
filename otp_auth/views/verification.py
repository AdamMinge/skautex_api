# Third-Party import
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import views, status
# Local import
from otp_auth.swagger import JWTResponseSerializer
from otp_auth.utils import create_refresh_token, verify_token
from otp_auth.policies import DeviceVerifyAccessPolicy
from otp_auth.signals import user_verified


class DeviceVerifyView(views.APIView):
    permission_classes = (DeviceVerifyAccessPolicy,)

    @swagger_auto_schema(responses={201: JWTResponseSerializer()})
    def post(self, request, token, *args, **kwargs):
        user = request.user
        device = verify_token(request.user, token)
        if device is not None:
            refresh_token = create_refresh_token(user, device)
            user_verified.send(sender=DeviceVerifyView, user=user, request=request)
            return Response({'refresh': str(refresh_token),
                             'access': str(refresh_token.access_token)},
                            status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
