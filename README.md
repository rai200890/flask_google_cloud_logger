# flask_google_cloud_logger
[![CircleCI](https://circleci.com/gh/rai200890/flask_google_cloud_logger.svg?style=svg&circle-token=3b2eb197f30dc714a6ba81167ddcf4e10a8c92a6)](https://circleci.com/gh/rai200890/flask_google_cloud_logger)
[![Maintainability](https://api.codeclimate.com/v1/badges/937c9f897f2cf89b9918/maintainability)](https://codeclimate.com/github/rai200890/flask_google_cloud_logger/maintainability)

Flask extension to format logs according to Google Cloud v2 Specification

Python log formatter for Google Cloud according to [v2 specification](https://cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) using [python-json-logger](https://github.com/madzak/python-json-logger) formatter

Inspired by Elixir's [logger_json](https://github.com/Nebo15/logger_json) 

## Instalation

### Pipenv

```
    pipenv install flask_google_cloud_logger 
```

### Pip

```
    pip install flask_google_cloud_logger 
```

## Usage

```python
import logging
from logging import config

from flask import Flask, request, g
from flask_google_cloud_logger import FlaskGoogleCloudLogger


LOG_CONFIG = {
    "version": 1,
    "formatters": {
        "json": {
            "()": "flask_google_cloud_logger.FlaskGoogleCloudFormatter",
            "application_info": {
                "type": "python-application",
                "name": "Example Application"
            },
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        }
    },
    "handlers": {
        "json": {
            "class": "logging.StreamHandler",
            "formatter": "json"
        }
    },
    "loggers": {
        "root": {
            "level": "INFO",
            "handlers": ["json"]
        },
        "werkzeug": {
            "level": "WARN",  # Disable werkzeug hardcoded logger
            "handlers": ["json"]
        }
    }
}

config.dictConfig(LOG_CONFIG) # load log config from dict
logger = logging.getLogger("root") # get root logger instance
app = Flask("test_app")
FlaskGoogleCloudLogger(app)


@app.route("/")
def hello_world():
    return "Hello, World!"


@app.teardown_request
def log_request_time(_exception):
    logger.info(f"{request.method} {request.path} - Sent {g.response.status_code} in {g.request_time:.5f}ms")
```

Example output:

```json
{"timestamp": "2018-11-04T21:34:04.002000Z", "severity": "INFO", "message": "GET / - Sent 200 in 0.13828ms", "labels": {"client": {"user_agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36", "ip": "127.0.0.1", "version": null}, "connection": {"method": "GET", "path": "/", "request_id": "9135a0fc-8398-40a7-b830-47f6265672a2", "status": 200}, "latency": 0.13828277587890625}, "metadata": {"userLabels": {}}, "sourceLocation": {"file": "test_app.py", "line": 51, "function": "log_request_time"}}
```

## Credits

Thanks [@thulio](https://github.com/thulio), [@robsonpeixoto](https://github.com/robsonpeixoto), [@ramondelemos](https://github.com/ramondelemos)
