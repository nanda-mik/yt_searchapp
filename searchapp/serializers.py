from rest_framework import serializers

from searchapp import models as app_models


class VideoStoreSerializer(serializers.ModelSerializer):
    """
    Model serializer for videostore model.
    """
    publishedAt = serializers.DateTimeField(source='publish_datetime')

    class Meta:
        model = app_models.VideoStore
        fields = (
            'title',
            'description',
            'publishedAt',
            'thumbnails'
        )


class VideoStoreListSerializer(VideoStoreSerializer):
    """
    List serializer using base videostore serializer as parent 
    to list videos.
    """

    class Meta(VideoStoreSerializer.Meta):
        fields = VideoStoreSerializer.Meta.fields + (
            '_created_on',
        )
