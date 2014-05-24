from functools import wraps
from flask import request, Response

def check_auth(username, password):
	return username == 'admin' and password == 'secret'

def authenticate():
	return Response(
	'Could not verify your access level for the current URL.\n'
	'You have to use the login credentials to access this URL', 401,
	{'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not check_auth(auth.username, auth.password):
			return authenticate()
		return f(*args, **kwargs)
	return decorated