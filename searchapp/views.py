from rest_framework.generics import ListAPIView

from searchapp import (
    models as app_models,
    serializers as app_serializers
)

# Create your views here.

class VideoStoreListView(ListAPIView):
    """
    View to list videos from store.
    """

    queryset = app_models.VideoStore.objects.all()
    serializer_class = app_serializers.VideoStoreListSerializer
