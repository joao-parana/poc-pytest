import requests
from requests.models import Response

class Stack:
    def __init__(self):
        self._storage = []
        self._URL = "http://some-remote-host:9740/storage"

    def __len__(self):
        return len(self._storage)

    def push(self, item):
        PARAMS = {'item':item}
        self._storage.append(item)
        r = requests.get(url = self._URL, params = PARAMS)
        # extracting data in json format
        data = r.json()
        self.write_for_debug(str(data))

    def pop(self):
        ret = None
        try:
            ret = self._storage.pop()
        except IndexError:
            pass
        return ret
    
    def write_for_debug(self, data):
        file = open("/tmp/push.txt", "w")
        file.write('requests.get: ' + str(data))
        file.close()
