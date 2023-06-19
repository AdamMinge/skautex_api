from core.mixins.multi_serializer import MultiSerializerViewSetMixin
from core.mixins.multi_permission import MultiPermissionViewSetMixin
from core.mixins.upload_file_model import UploadFileModelMixin
from core.mixins.create_model import CreateModelMixin
from core.mixins.update_model import UpdateModelMixin
from core.mixins.list_model import ListModelMixin
from core.mixins.retrieve_model import RetrieveModelMixin
from core.mixins.destroy_model import DestroyModelMixin

__all__ = ['MultiSerializerViewSetMixin', 'MultiPermissionViewSetMixin', 'UploadFileModelMixin',
           'CreateModelMixin', 'UpdateModelMixin', 'ListModelMixin', 'RetrieveModelMixin', 'DestroyModelMixin']
