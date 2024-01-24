from rest_framework import serializers

from searchapp import models as app_models


class VideoStoreSerializer(serializers.ModelSerializer):
    """
    Serializer for videostore model.
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
