# -*- coding: utf-8 -*-
"""Tutorial on using the InfluxDB client."""

import argparse

from influxdb import InfluxDBClient

#
# from influxdb import InfluxDBClient
#
# json_body = [
#     {
#         "measurement": "cpu_load_short",
#         "tags": {
#             "host": "server01",
#             "region": "us-west"
#         },
#         "time": "2009-11-10T23:00:00Z",
#         "fields": {
#             "value": 0.64
#         }
#     }
# ]
#
# client = InfluxDBClient('localhost', 8086, 'telegraf', 'secretpassword', 'mydb')
# client.create_database('mydb')
# client.write_points(json_body)
# result = client.query('select value from cpu_load_short;')
#
# print("Result: {0}".format(result))