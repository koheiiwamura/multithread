import threading
import time
import requests


def get_auth_token():
    data = '{"user_id": "", "password": "", "reuse": true}'
    response = requests.post('', data=data)
    return response.json()['result']['auth_token']

headers = {
    'Authorization': get_auth_token(),
}

info_data = ''


class MyThread(threading.Thread):

    def __init__(self, headers, info_data, url):
        threading.Thread.__init__(self)
        self.headers = headers
        self.info_data = info_data
	self.url = url

    def run(self):
        requests.post(self.url, headers=headers, data=info_data)


threads = []
for i in range(100):
    threads.append(MyThread(headers, info_data, url))

start = time.time()
for th in threads:
    th.start()
elapsed_time = time.time() - start
print(elapsed_time)
