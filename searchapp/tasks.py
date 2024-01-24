import logging
from celery import shared_task

from constance import config as live_setings

from searchapp import (
    exception as app_exceptions,
    models as app_models,
    serializers as app_serializers,
    utils as app_utils
)
from searchapp.youtube import Youtube

logger = logging.getLogger(__name__)


@shared_task
def fetch_and_store_yt_videos(**kwargs):
    """
    Task to fetch and store youtube videos using yt client.
    """

    lastpush_obj = app_models.LastPushDatetime.objects.first()

    if not lastpush_obj:
        logger.error("last push datetime obj not found!!")
        return

    query_str = live_setings.QUERY_STRING
    query_dt = lastpush_obj.video_success_dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    max_results = live_setings.MAX_RESULTS

    try:
        results = Youtube(
            query_str=query_str,
            query_dt=query_dt,
            max_results=max_results
        ).search_videos()
    except app_exceptions.YoutubeException as exc:
        logger.error(f"Failed to search videos due to: {exc}")
        return

    if not results:
        logger.error("No results found!!")
        return
    
    parsed_results = app_utils.parse_youtube_videos(results)
    serializer = app_serializers.VideoStoreSerializer(
        data=parsed_results,
        many=True
    )

    if not serializer.is_valid():
        logger.error(f"Validation failed for results: {serializer.errors}")
        return

    serializer.save()

    # fetch the latest video from the parsed results and update success date.
    latest_video = parsed_results[0]
    lastpush_obj.update_success_dt(
        new_dt=latest_video.get('publishedAt')
    )

    logger.info("Successfully pushed latest videos to store!!")
