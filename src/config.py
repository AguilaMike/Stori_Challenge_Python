import os

class Config:
    EMAIL_HOST = os.environ.get("EMAIL_HOST")
    EMAIL_PORT = os.environ.get("EMAIL_PORT")
    EMAIL_USER = os.environ.get("EMAIL_USER")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
    DATABASE_URL = os.environ.get("DATABASE_URL")
    EMAIL_TO = os.environ.get("EMAIL_TO")

config = Config()