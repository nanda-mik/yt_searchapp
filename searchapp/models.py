from django.db import models


class VideoStore(models.Model):
    """
    Model to store youtube videos with fields like title, description,
    publishat and thumbnails.
    Further enhancement: May add type field to models to store videos according
    to type and filter based on types(cricket, football,...etc)
    """

    _created_on = models.DateTimeField(
        auto_now_add=True,
        help_text="Datetime when the video is added to store."
    )
    title = models.TextField(
        help_text="Title of the video."
    )
    description = models.TextField(
        blank=True,
        null=True,
        help_text="Description of the video."
    )
    publish_datetime = models.DateTimeField(
        help_text="Date when video was published."
    )
    thumbnails = models.JSONField(
        default=dict,
        help_text="links of thumbnails of different dimensions."
    )

    def __str__(self) -> str:
        return f"{self.title}"


class LastPushDatetime(models.Model):
    """
    Model to store last push_datetime. Datetime used to do a search
    on youtube search api.
    """

    video_success_dt = models.DateTimeField(
        help_text="Datetime till which videos were pushed to store."
    )

    def update_success_dt(self, new_dt):
        """
        Update new success dt after pushing to store.
        """
        self.video_success_dt = new_dt
        self.save()

    def __str__(self) -> str:
        return f"{self.video_success_dt}"


class YoutubeCreds(models.Model):
    """
    Model to store youtube API key and credentials.
    """

    name = models.CharField(
        max_length=50,
        help_text="Name of the api key."
    )
    api_key = models.CharField(
        max_length=80,
        help_text="Api key for youtube service."
    )
    api_service_name = models.CharField(
        max_length=30,
        default='youtube',
        help_text="Service name used for yt client."
    )
    api_version = models.CharField(
        max_length=20,
        default='v3',
        help_text='API version.'
    )
    is_exhausted = models.BooleanField(
        default=False,
        help_text="stores if quota is exceeded for the day."
    )

    def __str__(self) -> str:
        return f"{self.name}"
