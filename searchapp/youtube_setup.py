import os

from apiclient.discovery import build

from searchapp import constants


class Youtube:
    """
    Class to setup youtube api integration related things.
    """

    def __init__(self):
        """
        
        """
        self.api_key = os.environ.get('YT_API_KEY', '')
        self.api_service_name = "youtube"
        self.api_version = "v3"
        self.yt_client = build(
            self.api_service_name, 
            self.api_version, 
            developerKey=self.api_key
        )

    def search_videos(self, query_str, query_dt, max_results=25):
        """
        
        """
        try:
            search_result = self.yt_client.search().list(
                q=query_str, 
                part=constants.YT_PART,
                type=constants.YT_TYPE,
                order=constants.YT_ORDER,
                publishedAfter=query_dt,
                relevanceLanguage=constants.YT_LANG,
                maxResults = max_results
            ).execute()
        except Exception as exc:
            print("Failed to query!")

        results = search_result.get("items", [])
        return results
