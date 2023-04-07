import requests
import pytest

@pytest.mark.smoke
def test_post_request():
    url = "http://127.0.0.1:8305/uploadfile/"
    files = { 
        "file": 
        open("tests/data/FortiClientVPNOnlineInstaller.exe", "rb") 
    }
    response = requests.post(url, files=files)
    assert(response.json() == {"filename": "FortiClientVPNOnlineInstaller.exe"})

