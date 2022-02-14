import os


class Config:
    CONFIG_NAME = 'base'
    CLIENT_ID = os.getenv('CLIENT_ID')
    CLIENT_SECRET = os.getenv('CLIENT_SECRET')
    STRAVA_UPLOAD_URL='https://www.strava.com/api/v3/uploads'
    STRAVA_TOKEN_REQUEST_URL='https://www.strava.com/oauth/token'
    DEVICE='IGPSPORT50E'


class LocalConfig(Config):
    CONFIG_NAME = 'local'


CONFIGS = [LocalConfig]

config_by_name = {cfg.CONFIG_NAME: cfg for cfg in CONFIGS}
