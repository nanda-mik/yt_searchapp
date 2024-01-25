from django.contrib import admin

from searchapp import models as app_models


# Register your models here.
@admin.register(app_models.VideoStore)
class VideoStoreAdmin(admin.ModelAdmin):
    """
    **BONUS POINT**
    Admin with search, ordering and filter support for video store.
    """

    search_fields = ['title', 'description']
    list_display = ['title', 'description', 'publish_datetime']
    ordering = ['-publish_datetime']
    list_filter = ['publish_datetime']


@admin.register(app_models.LastPushDatetime)
class LastPushDatetimeAdmin(admin.ModelAdmin):
    """
    Admin for Lastpushdatetime model.
    """
    list_display = ['video_success_dt']


@admin.register(app_models.YoutubeCreds)
class YoutubeCredsAdmin(admin.ModelAdmin):
    """
    Admin for youtube creds model.
    """
    list_display = ['name']
