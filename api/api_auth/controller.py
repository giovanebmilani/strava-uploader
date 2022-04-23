from flask import Blueprint, request
import json

from .service import AuthService
from .model import Token
#from ..utils.http import HTTP

auth = Blueprint('auth', __name__)
	
@auth.route('/auth', methods=['GET'])
def exchange_token() -> Token:
	code = request.args.get('code')
	if code:
		return json.dumps(AuthService.exchange_token(code).__dict__)#, HTTP.success
	return { 'message': 'Code is missing.'}#, HTTP.bad_request
