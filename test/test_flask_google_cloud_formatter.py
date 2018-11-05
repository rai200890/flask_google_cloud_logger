import pytest

from flask_google_cloud_logger import FlaskGoogleCloudFormatter


@pytest.fixture
def formatter():
    return FlaskGoogleCloudFormatter(application_info={
        "type": "python-application",
        "application_name": "Example Application"
    })


def test_make_labels_when_request_context_isnt_available(formatter, mocker):
    assert formatter.make_labels() == {
        "type": "python-application",
        "application_name": "Example Application"
    }


def test_make_metadata_when_request_context_is_available(formatter, mocker):
    mocker.patch(
        "flask_google_cloud_logger.formatter.has_request_context",
        return_value=True)
    request_mock = mocker.patch("flask_google_cloud_logger.formatter.request")

    request_mock.remote_addr = "0.0.0.0"
    request_mock.method = "GET"
    request_mock.path = "/"
    request_mock.headers = {
        "User-Agent": "Browser",
        "X-Request-ID": "4353658",
        "X-API-Version": "1"
    }

    g_mock = mocker.patch("flask_google_cloud_logger.formatter.g")

    g_mock.status_code = 200
    g_mock.request_time = 0.01
    g_mock.response = mocker.Mock(status_code=200)
    metadata = formatter.make_labels()

    assert metadata == {
        "client": {
            "ip": "0.0.0.0",
            "user_agent": "Browser",
            "version": "1"
        },
        "connection": {
            "method": "GET",
            "path": "/",
            "request_id": "4353658",
            "status": 200
        },
        "latency": 0.01,
        "type": "python-application",
        "application_name": "Example Application"
    }
