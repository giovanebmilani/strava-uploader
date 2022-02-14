import os


class Config:
    CONFIG_NAME = 'base'
    CLIENT_ID = '69535'
    CLIENT_SECRET = 'bac246d8c108ae3a6f7682be186105d513e33727'
    REDIRECT_URI = 'http://127.0.0.1:5000/authorized'
    
    STRAVA_AUTH_URL = 'http://www.strava.com/oauth/authorize'
    STRAVA_TOKEN_REQUEST_URL = 'https://www.strava.com/oauth/token'
    STRAVA_UPLOAD_URL = 'https://www.strava.com/api/v3/uploads'

    DEVICE='IGPSPORT50E'


class LocalConfig(Config):
    CONFIG_NAME = 'local'


CONFIGS = [LocalConfig]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in CONFIGS}
