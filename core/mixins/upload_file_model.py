# Third-Party import
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.parsers import MultiPartParser


class UploadFileModelMixin(object):
    @action(detail=True, methods=['PUT'], parser_classes=[MultiPartParser])
    def upload_file(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = self.get_serializer_class()(obj, data=request.data,
                                                 partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

