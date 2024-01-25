# YT Search

## Basic Installation
* Asumming you have python & pip installed on your device. If not, please install it.
* After doing above, install virtualenv and create a virtual environment.
    ```bash
        $ pip install virtualenv
        $ python3 -m venv venv
    ```
* Then clone this repo(Below is using https):
    ```bash
        $ git clone https://github.com/nanda-mik/yt_searchapp.git
    ```


* #### Steps to follow(To run the application in local)
    1. cd into the cloned repo:
        ```bash
            $ cd yt_searchapp
        ```
    2. Activate your virtual environment:
        ```bash
            $ source venv/bin/activate
        ```
    3. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt --upgrade
        ```
    4. Install PostgreSQL and create database for the required project.
        ```bash
            Follow this: https://www.codementor.io/@engineerapart/getting-started-with-postgresql-on-mac-osx-are8jcopb
        ```
    5. Install Redis and start the service.
        ```bash
            Follow this:
            https://redis.io/docs/install/install-redis/install-redis-on-mac-os/
        ```
    6. Create a google api key for the yt client:
        ```bash
            Follow this: https://developers.google.com/youtube/v3/docs
        ```
    6. Set Environment Values:
        * Copy the .env_template to .env
        * Fill the values of .env as required.
    7. Apply migrations:
        ```bash
            $ python manage.py migrate
        ```
    8. Apply fixture required for the project:
        ```bash
            python manage.py load_fixture
        ```
    9. Create superuser for admin.
        ```bash
            python manage.py createsuperuser
        ```
    9. Create Youtube creds: 
        * Refer below *API's & functionalities* section to know how to create creds in youtube store.
    8. To run server locally using the below command:
        ```bash
            $ python manage.py runserver
        ```
    9. To run celery worker in local, open another terminal and run this command:
        ```bash
            $ celery -A <app>.celery worker -l INFO
        ```
    10. To run celery beat in local, open another terminal and run this command:
        ```bash
            $ celery -A <app>.celery beat -l INFO
        ```
    11. To run unit test cases on local:
        ```bash
            $ python manage.py test
        ```


* #### Running the app in Docker
    To run the app, you need to perform two steps:

    1. #### Build the image: 
    This is done using the build command, which uses the Dockerfile you just created. To build the image, run the command below:
    ```bash
    docker build . -t docker-django-v1.0
    ```
    This command should be executed in the directory where the Docker file lives. The -t flag tags the image so that it can be referenced when you want to run the container.
 
    2. #### Run the image:
    This is done using the docker run command. This will convert the built image into a running container. To run the app, execute the below command:
    ```bash
        docker run docker-django-v1.0
    ```
    You can proceed to view your app in the browser at localhost:8000.

    Follow this to dockerize a simple django app:
    https://blog.logrocket.com/dockerizing-django-app/


* ### Modules and api's
    1. #### Models:
        - VideoStore: Stores video data like titile, description, etc.
        - LastPushDatetime: Stores last datetime till which data is pushed to store.
        - YoutubeCreds: Stores multiple api keys with exhausted criteria.
    2. #### Serializers & views:
        - Serializer to validate data data before storing and for List API's
        - View for video store to list with search and ordering support.
    3. #### API's & functionalities:
        - Admin endpoint: Login to admin using the superuser created earlier. This gives you a UI/dashboard to interact with your models by django.
        ```bash
            http://127.0.0.1:8000/admin
        ```
        - Use the above admin to create creds using api_name, key, service_name & version. This will be used to fetch videos from youtube.
        - Background task: A periodic task runs in a 5minute interval which fetch videos from youtube and store it to our db based on query.
        - List Video: This will list all videos in descending order of their published time with a pagination of page_size=10.
        ```bash
            http://127.0.0.1:8000/api/videos/
        ```
        - Search videos: Add query params for searching a particular content from title/description like this:
        ```bash
            http://127.0.0.1:8000/api/videos?q=hello
        ```
        This will search all videos whose title/description which contains hello.
        It also supports partial search.

* Hope this documentation will help you to run the project!!
