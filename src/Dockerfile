FROM python:alpine
COPY main.py /
RUN pip install requests influxdb-client  schedule
CMD ["python","main.py"]
