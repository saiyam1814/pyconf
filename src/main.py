from influxdb_client import InfluxDBClient, Point, WritePrecision
from datetime import datetime
from influxdb_client.client.write_api import SYNCHRONOUS
import schedule
import time
import socket
import os

def influx():
    print("starting")
    org = "test"
    bucket = "test"
    print("{}".format(os.environ.get('token')))
    client = InfluxDBClient(url="http://185.136.234.159:30305", token="{}".format(os.environ.get('token')))

    write_api = client.write_api(write_options=SYNCHRONOUS)
    point = Point("mem").tag("host", "host1").field("used_percent", 23.43234543).time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket, org, point)

schedule.every(5).seconds.do(influx)   
while 1:
    schedule.run_pending()
    time.sleep(1)
