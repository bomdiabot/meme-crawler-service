import json
import requests


class Client(object):
    api_url = 'http://35.226.124.10:7310/'
    def __init__(self, user=None, password=None):
        if user is None or password is None:
            raise ValueError('User and password are obrigatory')
        payload = {'username': user, 'password': password}
        try:
            r = requests.post(self.api_url + 'auth/login', data=payload)
            self.access_token = r.json()['access_token']
        except ValueError:
            print("Invalid user or password")
        print(self.access_token)
    
    def post(self, route, payload):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + self.access_token
        }
        return requests.post(self.api_url + route, headers=headers, data=payload)

    def post_text(self, text, src):
        payload = {}
        payload['content'] = text
        payload['tags'] = 'bomdia,src:{}'.format(src)
        data = json.dumps(payload)
        r = self.post('texts', data)
        print(r.json())