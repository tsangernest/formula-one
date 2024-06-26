FROM python:3.12.3


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /app
COPY requirements.txt .


WORKDIR /var
RUN python3 -m venv venv/


RUN cd /var/venv/
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


WORKDIR /app
COPY . .


RUN python manage.py migrate


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

