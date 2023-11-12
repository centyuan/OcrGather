import os
from datetime import datetime
from wsgiref.handlers import format_date_time
from time import mktime
import hashlib
import base64
import hmac
from urllib.parse import urlencode
import json
import requests
import logging
import traceback

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

class UrlException(Exception):
    def __init__(self, msg):
        self.message = msg


def sha256base64(data):
    sha256 = hashlib.sha256()
    sha256.update(data)
    digest = base64.b64encode(sha256.digest()).decode(encoding='utf-8')
    return digest


def parse_url(requset_url):
    """
    解析url
    :param requset_url:
    :return:
    """
    stidx = requset_url.index("://")
    host = requset_url[stidx + 3:]
    schema = requset_url[:stidx + 3]
    edidx = host.index("/")
    if edidx <= 0:
        raise UrlException("invalid request url:" + requset_url)
    path = host[edidx:]
    host = host[:edidx]
    return host, path, schema


def xfyun_token(requset_url, method="POST", api_key="", api_secret=""):
    """
    鉴权 并返回request url
    :param requset_url:
    :param method:
    :param api_key:
    :param api_secret:
    :return:
    """
    host, path, schema = parse_url(requset_url)
    # 转为RFC1123日期格式
    date = format_date_time(mktime(datetime.now().timetuple()))
    signature_origin = "host: {}\ndate: {}\n{} {} HTTP/1.1".format(host, date, method, path)
    """
    signature原始字段(signature_origin)则为：
        host: api.xf-yun.com
        date: Wed, 11 Aug 2021 06:55:18 GMT
        POST /v1/private/sf8e6aca1 HTTP/1.1
    """
    # 生成摘要
    signature_sha = hmac.new(api_secret.encode('utf-8'), signature_origin.encode('utf-8'),
                             digestmod=hashlib.sha256).digest()
    # 对摘要编码
    signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
    authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
        api_key, "hmac-sha256", "host date request-line", signature_sha)
    authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
    values = {
        "host": host,
        "date": date,
        "authorization": authorization
    }
    return requset_url + "?" + urlencode(values)


class XFyunApi:
    def __init__(self, api_key, secret_key,app_id=None,level=1):
        """
        :param api_key:
        :param secret_key:
        """
        self.app_id = app_id
        self.api_key = api_key
        self.secret_key = secret_key
        self.level = level
        self.url = 'http://api.xf-yun.com/v1/private/hh_ocr_recognize_doc'
        # self.url = 'https://api.xf-yun.com/v1/private/sf8e6aca1'

    def get_text(self, file_path=None, file_url=None):
        try:
            image_data = None
            if file_path and os.path.exists(file_path):
                with open(file_path, "rb") as f:
                    image_data = f.read()
            elif file_url:
                image_data = get_picture(file_url)
            if image_data:
                body = {
                    "header": {
                        "app_id": self.app_id,
                        "status": 3
                    },
                    "parameter": {
                        "sf8e6aca1": {
                            "category": "ch_en_public_cloud",
                            "result": {
                                "encoding": "utf8",
                                "compress": "raw",
                                "format": "json"
                            }
                        }
                    },
                    "payload": {
                        "sf8e6aca1_data_1": {
                            "encoding": "jpg",
                            "image": str(base64.b64encode(image_data), 'UTF-8'),
                            "status": 3
                        }
                    }
                }
                request_url = xfyun_token(self.url, "POST", self.api_key, self.secret_key)

                headers = {'content-type': "application/json", 'host': 'api.xf-yun.com', 'app_id': self.app_id}
                response = requests.post(request_url, data=json.dumps(body), headers=headers)
                if response.status_code !=200:
                    logging.error(f"error:{response.json()}")
                    return False, f"error:{response.json()}"
                tempResult = json.loads(response.content.decode())
                finalResult = base64.b64decode(tempResult['payload']['result']['text']).decode()
                if finalResult:
                    finalResult = finalResult.replace(" ", "").replace("\n", "").replace("\t", "").strip()
                    text = eval(finalResult)['pages'][0]['lines'][1]['words'][0]['content']
                    return True, text
                else:
                    return False, None
        except Exception as e:
            logging.error(traceback.format_exc())
            return False, str(e)



if __name__ == '__main__':
    app_id = "eb78ba1a"  
    api_key = os.getenv("API_KEY", "618642319dd26346780f676e9f9dfad9") 
    secret_key = os.getenv("SECRET_KEY", "ZmM3Mjc4NjcyNjcyYmJiNGZmNmU5NmNh")
    file_path = "../assets/1c3d.png"
    client = XFyunApi(app_id, api_key, secret_key)
    mark, text = client.get_text(file_path=file_path)
    print(mark,text)
