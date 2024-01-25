from django.urls import reverse
from django.test import tag
from django_dynamic_fixture import G
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from searchapp import models as app_models


@tag('video_store')
class TestVideoStoreListView(APITestCase):
    """
    Test case for Video store list view.
    #EXTRA apart from bonus.
    """

    client = APIClient()

    def setUp(self) -> None:
        self.inst1 = G(
            app_models.VideoStore,
            title='Test title 1',
            description='Hello world',
            publish_datetime='2023-12-04 12:00:00'
        )
        self.inst2 = G(
            app_models.VideoStore,
            title='Clone 2',
            description='i am a clone.',
            publish_datetime='2023-12-01 14:00:00'
        )
        return super().setUp()

    def get_url(self):
        """
        Create and return url using reverse lookup from the name.
        """
        return reverse('list_video')
    

    def test_list_all_videos(self):
        """
        Test case to check get api with all videos.
        """
        response = self.client.get(
            self.get_url()
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        res = response.json()
        self.assertEqual(
            res.get('count'),
            2
        )

    def test_search_videos_1(self):
        """
        Test case to check if search works.
        """
        response = self.client.get(
            f"{self.get_url()}?q=title"
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        res = response.json()
        self.assertEqual(
            res.get('count'),
            1
        )
        self.assertEqual(
            res.get('results')[0].get('title'),
            self.inst1.title
        )

    def test_videos_ordering(self):
        """
        Test case to check if the videos are in ordering of
        publish datetime. 
        """
        response = self.client.get(
            self.get_url()
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        res = response.json()
        self.assertEqual(
            res.get('count'),
            2
        )
        self.assertEqual(
            res.get('results')[0].get('title'),
            self.inst1.title
        )

        # change the inst2 publishat
        self.inst2.publish_datetime = '2024-01-01 14:00:00'
        self.inst2.save()

        response = self.client.get(
            self.get_url()
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        res = response.json()
        self.assertEqual(
            res.get('count'),
            2
        )
        self.inst2.refresh_from_db()
        self.assertEqual(
            res.get('results')[0].get('title'),
            self.inst2.title
        )
