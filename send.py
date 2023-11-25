import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

url = 'http://csbnpmnk-5000.asse.devtunnels.ms/upload'
file_path = 'hasil/video_501.mp4'

try:
    response = requests.post(url, files={'file': open(file_path, 'rb')}, verify=False)
    print(response.status_code)
    print(response.text)
except requests.exceptions.SSLError as e:
    print(f"SSLError: {e}")
except requests.exceptions.RequestException as e:
    print(f"RequestException: {e}")