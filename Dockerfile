FROM python:3.11.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY . /app

COPY /templates /templates

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

#Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
