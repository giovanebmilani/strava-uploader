import webbrowser

client_id = '69535'
client_secret = 'bac246d8c108ae3a6f7682be186105d513e33727'
redirect_uri = 'http://127.0.0.1:5000/authorized'
scopes = 'activity:write,read_all'

auth_url = 'http://www.strava.com/oauth/authorize?client_id='+client_id+'&response_type=code&redirect_uri='+redirect_uri+'&approval_prompt=force&scope='+scopes

def authenticate():
    webbrowser.open(auth_url)


if __name__ == '__main__':
    authenticate()
