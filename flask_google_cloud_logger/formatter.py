import uuid

from flask import g, has_request_context, request

from google_cloud_logger import GoogleCloudFormatter


class FlaskGoogleCloudFormatter(GoogleCloudFormatter):
    def __init__(self, *args, **kwargs):
        super(FlaskGoogleCloudFormatter, self).__init__(*args, **kwargs)

    def make_labels(self):
        data = self.application_info or {}
        if has_request_context():
            data = {
                **data,
                **{
                    "client": self._make_client_info(request),
                    "connection": self._make_connection_info(request, g),
                    "latency": getattr(g, "request_time", None)
                }
            }
        return data

    def _make_client_info(self, request):
        return {
            "user_agent": request.headers.get("User-Agent"),
            "ip": request.headers.get("X-Forwarded-For")
            or request.remote_addr,
            "version": request.headers.get("X-API-Version")
        }

    def _make_connection_info(self, request, g):
        return {
            "method": request.method,
            "path": request.path,
            "request_id": request.headers.get("X-Request-ID") or uuid.uuid4(),
            "status":
            g.response.status_code if hasattr(g, "response") else None
        }
