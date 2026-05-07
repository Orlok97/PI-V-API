from controllers.test import test_bp
from controllers.sensor import sensor_bp

class Router:
    def __init__(self,app):
        self.app=app
        self.routes()
    def routes(self):
        self.app.register_blueprint(test_bp,url_prefix="/api/v1/test")
        self.app.register_blueprint(sensor_bp, url_prefix="/api/v1/sensor")