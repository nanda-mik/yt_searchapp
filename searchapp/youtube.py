import logging

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError, Error

from searchapp import (
    constants as app_constants,
    exception as app_exceptions,
    models as app_models
)

logger = logging.getLogger(__name__)


class Youtube:
    """
    Class to setup youtube api integration and its functionalities.
    """

    def __init__(self, query_str, query_dt, max_results=25):
        """
        Init method to setup youtube client.
        """
        self.yt_cred = app_models.YoutubeCreds.objects.filter(
            is_exhausted=False
        ).first()

        if not self.yt_client:
            raise app_exceptions.YoutubeException("Quota exceeded for all keys!!")

        self.api_key = self.yt_cred.api_key
        self.api_service_name = self.yt_cred.api_service_name
        self.api_version = self.yt_cred.api_version

        # initialize youtube client.
        try:
            self.yt_client = build(
                self.api_service_name, 
                self.api_version, 
                developerKey=self.api_key
            )
        except Error as exc:
            logger.exception(f"Failed to connect due to: {exc}")
            raise app_exceptions.YoutubeException("Building yt client failed!!")

        self.query_str = query_str
        self.query_dt = query_dt
        self.max_results = max_results

    def search(self, query_type):
        """
        Query on youtube search api based on received parameters.
        """
        try:
            search_result = self.yt_client.search().list(
                q=self.query_str, 
                part='ada',
                type=query_type,
                order=app_constants.YT_ORDER,
                publishedAfter=self.query_dt,
                relevanceLanguage=app_constants.YT_LANG,
                maxResults = self.max_results
            ).execute()
        except HttpError as error:
            response = error.resp
            message = error._get_reason()

            if response.status == 403 and 'quotaExceeded' in message:
                logger.error(f"Quota exhausted for this api key: {self.api_key.name}")
                self.yt_cred.is_exhausted = True
                self.yt_client.save()
                return
            else:
                raise app_exceptions.YoutubeException(f"Failed to search due to: {message}")
        
        return search_result

    def search_videos(self):
        """
        Search videos using youtube client based on the query.      
        """

        search_results = self.search(app_constants.YT_TYPE)
        results = search_results.get("items", [])

        return results
