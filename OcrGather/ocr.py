from OcrGather.clients import *


class Client():
    def __init__(self):
        self.supported_clients = {
            'aliyun': AliyunApi,
            'tencent': TecentApi,
            'baidu': BaiduApi,
            'textin': TextinApi,
            'youdao': YoudaoApi,
            'xfyun': XFyunApi,
            'tesseract': TesseractOcr,
        }
        for k, v in self.supported_clients.items():
            setattr(self, k, v)
