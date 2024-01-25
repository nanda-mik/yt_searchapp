# YT Search

## Installation
* Hope you have a python & pip installed on your device. If not, please install it.
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
    docker build . -t docker-django-v0.0
    ```
    This command should be executed in the directory where the Docker file lives. The -t flag tags the image so that it can be referenced when you want to run the container.
 
    2. #### Run the image:
    This is done using the docker run command. This will convert the built image into a running container. To run the app, execute the below command:
    ```bash
        docker run docker-django-v0.0
    ```
    You can proceed to view your app in the browser at localhost:8000.

    Follow this to dockerize a simple django app:
    https://blog.logrocket.com/dockerizing-django-app/
