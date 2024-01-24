import logging
from celery import shared_task

logger = logging.getLogger(__name__)


@shared_task
def fetch_and_store_yt_videos(**kwargs):
    """
    """

    logger.info("executed!!!")
