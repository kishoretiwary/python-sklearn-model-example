FROM python:3.7.5-stretch
WORKDIR /app
ADD . /app
RUN pip3 install -r ./requirements.txt
EXPOSE 8000
CMD ["gunicorn", "main:app","-b","0.0.0.0:8000"]
