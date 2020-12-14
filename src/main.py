from influxdb_client import InfluxDBClient, Point, WritePrecision
from datetime import datetime
from influxdb_client.client.write_api import SYNCHRONOUS
import schedule
import time
import socket
import os

def influx():
    print("starting")
    org = "demo"
    bucket = "demo"
    client = InfluxDBClient(url="{}".format(os.environ.get('host')), token="{}".format(os.environ.get('token')))
    meminfo = dict((i.split()[0].rstrip(':'),int(i.split()[1])) for i in open('/proc/meminfo').readlines())
    freemem = meminfo['MemFree'] / 1024 /1024
    write_api = client.write_api(write_options=SYNCHRONOUS)
    point = Point("free_mem").tag("host", socket.gethostname()).field("free_memory_Gb", freemem ).time(datetime.utcnow(), WritePrecision.NS)
    write_api.write(bucket, org, point)

schedule.every(5).seconds.do(influx)   
while 1:
    schedule.run_pending()
    time.sleep(1)
