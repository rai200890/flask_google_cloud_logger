from flask import g

import flask_google_cloud_logger


def test_flask_google_cloud_logger_before_request(app_client, mocker):
    mocker.patch(
        "flask_google_cloud_logger.hooks.time",
        return_value=1540174450.9542747)
    with app_client.application.app_context():
        flask_google_cloud_logger.flask_google_cloud_logger_before_request()
        assert g.get("start_request") == 1540174450.9542747


def test_flask_google_cloud_logger_after_request(app_client, mocker):
    with app_client.application.app_context():
        response = app_client.get("/")
        mocker.patch(
            "flask_google_cloud_logger.hooks.time",
            return_value=1540175117.2246253)
        g.start_request = 1540174450.9542747
        flask_google_cloud_logger.flask_google_cloud_logger_after_request(
            response)
        assert g.get("request_time") == 666270.3506946564
        assert g.response == response
