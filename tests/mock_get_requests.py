class MockMyRequest:
    def __init__(self, url, item = None):
        pass

    def json(self):
        result = {
            "candidates": [
                {
                    "geolocation": {
                        "lat": -34.5453062,
                        "lng": -58.44977489
                    },
                    "name": "Estadio Monumental (Buenos Aires)"
                }
            ]}
        return result