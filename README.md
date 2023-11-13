# OcrGather

[![maintainer](https://img.shields.io/badge/Maintainer-centyuan-blue.svg)](https://github.com/centyuan)

![language](https://img.shields.io/badge/Language-Python-green.svg)

[![PyPI](https://img.shields.io/pypi/v/ocr-gather)](https://pypi.org/project/ocr-gather)

[![star](https://img.shields.io/github/stars/centyuan/ocr-gather.svg?style=social&label=Star)](https://github.com/centyuan/ocr-gather)

[![Fork](https://img.shields.io/github/forks/centyuan/centyuan.github.io.svg?style=social&label=Fork)](https://github/centyuan/ocr-gather)

[![Watch](https://img.shields.io/github/forks/centyuan/centyuan.github.io.svg?style=social&label=Watch)](https://github.com/centyuan/ocr-gather)

[![PyPI - Downloads](https://pepy.tech/badge/ocr-gather)](https://pypi.org/project/ocr-gather/)

## [OcrGather](https://github.com/centyuan/OcrGather#installation)

```
Some third-party OCR services are encapsulated
You can star this repository to keep track of the project if it's helpful for you, thank you for your support.
```

## [Installation](https://github.com/centyuan/OcrGather#installation)

**Pip install**

```
pip install OcrGather
```

## [Support List](https://github.com/centyuan/OcrGather#support-list)

| Service Name | Service Provider |  client name  | Support |
| :----------: | :--------------: | :-----------: | :-----: |
|   有道OCR    |       有道       | ocr.youdao()  |    Y    |
|   讯飞OCR    |       讯飞       |  ocr.xfyun()  |    Y    |
|   合合OCR    |     合合信息     | ocr.textin()  |    Y    |
|   腾讯OCR    |       腾讯       | ocr.tencent() |    Y    |
|   阿里OCR    |       阿里       | ocr.aliyun()  |    Y    |
|   百度OCR    |       百度       | ocr.aliyun()  |    Y    |
|  Tesseract   |                  |               |    X    |
|     ...      |       ...        |               |   ...   |



## [Quick Start](https://github.com/CharlesPikachu/DecryptLogin#quick-start)

```
from OcrGather import ocr 

# create instance 
api_key = os.getenv("API_KEY", "77f89e08f43a86f9")   # api key 
secret_key = os.getenv("SECRET_KEY", "HlmF4vlvwmemBL2tG4wIYiUob3BUjZQ1")  # secret key
client = ocr.youdao(api_key=api_key,secret_key=secret_key)
file_path =  "../assets/1c3d.png"
# 或  file_url ="https://xxx/xxx.png"
mark, text = client.get_text(file_path=file_path)
# 或 client.get_text(file_url=file_url)
```

