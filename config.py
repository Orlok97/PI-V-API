import os

from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self, app):
        self.app=app
        self.config()
        print('ok')
    def config(self):
        self.app.config["SQLALCHEMY_DATABASE_URI"]=os.getenv('DATABASE_URI')
        self.app.json.sort_keys=False