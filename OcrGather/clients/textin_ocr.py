import os
import requests

from OcrGather.clients.utils import get_picture

class TextinApi:
    def __init__(self, api_key, secret_key, level=1):
        self.url = 'https://api.textin.com/ai/service/v2/recognize'
        self.head = {
            'x-ti-app-id': api_key,
            'x-ti-secret-code': secret_key,
        }

    def get_text(self, file_path=None, file_url=None):
        try:
            image = None
            if file_path and os.path.exists(file_path):
                with open(file_path, 'rb') as f:
                    image = f.read()
            elif file_url:
                image = get_picture(file_url)
            else:
                return False, '图片为空'
            resp = requests.post(self.url, data=image, headers=self.head)
            result = resp.json()
            if result.get('code') == 200:
                return True, result['result']['lines'][0]['text']
            else:
                return False,result.get('message')
        except Exception as e:
            return False, e


if __name__ == "__main__":
    api_key = ""
    secret_key = ""
    file_path = "../assets/1c3d.png"
    client = TextinApi(api_key=api_key,secret_key=secret_key)
    mark,text = client.get_text(file_path=file_path)
