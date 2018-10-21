from time import time

from flask import g


def flask_google_cloud_logger_before_request():
    g.start_request = time()


def flask_google_cloud_logger_after_request(response):
    g.request_time = (time() - g.start_request) * 1000  # request time in ms
    g.response = response
    return response
