from django.urls import path

from searchapp import views as app_views


urlpatterns = [
    path(
        'videos/',
        app_views.VideoStoreListView.as_view(),
        name='list_video'
    )
]
