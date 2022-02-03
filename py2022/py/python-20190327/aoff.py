import requests
import time
while True:
    result = requests.get('http://angryoffers.info')
    print(result.ok)
    time.sleep(5)