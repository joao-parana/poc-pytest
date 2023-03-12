from requests.models import Response

class MockMyRequest:
    def __init__(self, url, item = None):
        self.url = url
        self.item = item

    def json(self):
        result = {
            "candidates": [ { 
                "geolocation": {
                    "lat": -23.0131038, "lng": -43.3965533 
                },
                "name": "Praia da Reserva",
                "plus_code": "XJQ5+3HR, Rio de Janeiro"
            }]}
        return result
    
    def getMock(self) -> Response:
        fake_response = Response()
        fake_response.status_code = 200
        fake_response.json = self.json
        return fake_response;
