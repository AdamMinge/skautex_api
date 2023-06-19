from rest_framework import serializers


class JWTResponseSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    access = serializers.CharField()
