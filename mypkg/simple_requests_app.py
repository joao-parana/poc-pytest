import requests
from requests.models import Response

class RemoteAPIAccess:
    def __init__(self, url):
        self._url = url

    def doGet(self, item) -> Response:
        PARAMS = {'item':item}
        r: Response = requests.get(url = self._url, params = PARAMS)
        return r

def do_get_httpbin():
    remoteAPIAccess = RemoteAPIAccess("https://httpbin.org/get")
    r: Response = remoteAPIAccess.doGet("teste")
    print(r.json())

def do_get_google():
    PARAMS = {'item':'Rio de Janeiro'}
    r: Response = requests.get(url = "https://google.com", params = PARAMS)
    print('status: ', r.status_code, 'value', r.json())
    return r
