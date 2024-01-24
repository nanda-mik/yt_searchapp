from django.contrib import admin

from searchapp import models as app_models


# Register your models here.
@admin.register(app_models.VideoStore)
class VideoStoreAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']
    list_display = ['title', 'description', 'publish_datetime']


@admin.register(app_models.LastPushDatetime)
class LastPushDatetimeAdmin(admin.ModelAdmin):
    list_display = ['video_success_dt']


@admin.register(app_models.YoutubeCreds)
class YoutubeCredsAdmin(admin.ModelAdmin):
    list_display = ['name']
