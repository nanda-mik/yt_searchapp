from django.db import models
from rest_framework import filters, generics

from searchapp import (
    models as app_models,
    serializers as app_serializers
)


class VideoStoreListView(generics.ListAPIView):
    """
    ListAPIView to list videos from store.
    """

    queryset = app_models.VideoStore.objects.all()
    serializer_class = app_serializers.VideoStoreListSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    ordering = ['-publish_datetime']
    filter_fields = ['title', 'description']

    def get_queryset(self):
        """
        **BONUS POINT**
        Override queryset to support partial search. 
        This can be improved just added a simple logic for now (Some cases may get missed.)
        """

        qs = super().get_queryset()
        search_query = self.request.query_params.get('q', None)

        # if search query is passed, do a ilike search on the store.
        if search_query:
            search_words = search_query.split()

            comb_q1 = models.Q()
            comb_q2 = models.Q()

            for word in search_words:
                comb_q1 &= models.Q(title__icontains=word)
                comb_q2 &= models.Q(description__icontains=word)
            
            qs = qs.filter(comb_q1 | comb_q2)

        return qs
