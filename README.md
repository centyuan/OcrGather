# OcrGather

<div align="center">
    <a href="https://github.com/centyuan"> <img src="https://img.shields.io/badge/Maintainer-centyuan-blue.svg"> 
    </a>
    <a href="">
        <img src="https://img.shields.io/badge/Language-Python-green.svg">
    </
    <a href="https://github.com/centyuan/OcrGather"><img src="https://img.shields.io/pypi/v/OcrGather"></a>
    <a href="https://pdm-project.org"><img src="https://img.shields.io/badge/pdm-managed-blueviolet"</a>
    <br>
    <a href=""><img src="https://img.shields.io/github/stars/centyuan/OcrGather.svg?style=social&label=Star"></a>
    <a href=""><img src="https://img.shields.io/github/forks/centyuan/OcrGather.svg?style=social&label=Fork"></a>
     <a href=""><img src="https://img.shields.io/github/forks/centyuan/OcrGather.svg?style=social&label=Watch"></a>
    <a href="https://pypi.org/project/OcrGather/"><img src="https://pepy.tech/badge/OcrGather"></a>
</div>

## [OcrGather](https://github.com/centyuan/OcrGather#OcrGather)

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
|   腾讯OCR    |       腾讯       | ocr.tencent() |    X    |
|   阿里OCR    |       阿里       | ocr.aliyun()  |    X    |
|   百度OCR    |       百度       | ocr.aliyun()  |    Y    |
|  Tesseract   |                  |               |    X    |
|     ...      |       ...        |               |   ...   |

## [Quick Start](https://github.com/centyuan/OcrGather#quick-start)

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
