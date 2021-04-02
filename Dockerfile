FROM python:3.8
WORKDIR /app
ENV FLASK_ENV=production
ENV FLASK_PORT=5000
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
ENTRYPOINT ["python" "main.py"]
#Dockerfile
