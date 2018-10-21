from flask import Flask
import pytest
from flask_google_cloud_logger import FlaskGoogleCloudLogger

app = Flask("test_app")
FlaskGoogleCloudLogger(app)


@pytest.fixture
def app_client():
    return app.test_client()
