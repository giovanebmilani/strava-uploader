import requests
import os

from .model import Token, Athlete

class AuthService:
	
	@staticmethod
	def exchange_token(code: str) -> Token:
		params = {
			'client_id': os.getenv('CLIENT_ID'),
			'client_secret': os.getenv('CLIENT_SECRET'),
			'grant_type': 'authorization_code',
			'code': code
		}
		res = requests.post('https://www.strava.com/oauth/token', params=params).json()
		token = Token(res['access_token'], res['refresh_token'], res['expires_at'])
		return token
