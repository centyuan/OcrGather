from OcrGather.clients import *
from DecryptLogin import login


class Client():
    def __init__(self):
        self.client_sdks = {
            'aliyun': AliyunApi,
            'tencent': TecentApi,
            'baidu': BaiduApi,
            'textin': TextinApi,
            'youdao': YoudaoApi,
            'xfyun': XFyunApi,
            'tesseract': TesseractOcr,
        }
        for k, v in self.client_sdks.items():
            setattr(self, k, v)
