FROM python:3.12.3


ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1


WORKDIR /


RUN python3 -m venv .venv/


COPY requirements.txt .


RUN pip install --no-cache-dir --upgrade -r requirements.txt


COPY . .


RUN python manage.py migrate


EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

