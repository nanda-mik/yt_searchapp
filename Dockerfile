# Dockerfile

FROM python:3.9

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --upgrade

EXPOSE 8000

COPY . code
WORKDIR /code

ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
