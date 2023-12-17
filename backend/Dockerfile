FROM python:3.11
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
CMD python /wait_for_initializer.py && python manage.py runserver 0.0.0.0:8000