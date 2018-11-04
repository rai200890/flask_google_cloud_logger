from . import hooks
from .formatter import FlaskGoogleCloudFormatter  # noqa


class FlaskGoogleCloudLogger(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)
            app.teardown_appcontext(self.teardown)

    def teardown(self, exception):
        if self.app.before_request_funcs is not None:
            self.app.before_request_funcs.pop(
                "flask_google_cloud_logger_before_request", None)
        if self.app.after_request_funcs is not None:
            self.app.after_request_funcs.pop(
                "flask_google_cloud_logger_after_request", None)

    def init_app(self, app):
        self.app.before_request(hooks.flask_google_cloud_logger_before_request)
        self.app.after_request(hooks.flask_google_cloud_logger_after_request)
