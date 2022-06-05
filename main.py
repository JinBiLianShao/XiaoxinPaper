# author ：Liansixin
import hashlib
import http
import json
import sys
import random
import os
import urllib
import requests
from translate import Translator
import http.client
import hashlib
import urllib
import random
import json

if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']

from mainWindow import Ui_MainWindow
from PyQt5.Qt import *


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.click_pushButton)

    def click_pushButton(self):
        tst = self.textEdit.toPlainText()
        tst = youdao_en(tst)
        print(tst)
        translation = trans_lang(tst)
        print(translation)
        self.textEdit_2.setText(translation)
        return


def youdao_en(query):
    url = 'http://fanyi.youdao.com/translate'
    data = {
        "i": query,  # 待翻译的字符串
        "from": "zh-CHS",
        "to": "en",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "16081210430989",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION"
    }
    res = requests.post(url, data=data).json()
    return res['translateResult'][0][0]['tgt']

def trans_lang(q):
    trans_result = q
    # 百度appid和密钥需要通过注册百度【翻译开放平台】账号后获得
    appid = '20211103000990117'  # 填写你的appid
    secretKey = 'LXQgIXAj9aoKoHGMA7zs'  # 填写你的密钥

    httpClient = None
    myurl = '/api/trans/vip/translate'  # 通用翻译API HTTP地址

    fromLang = 'auto'  # 原文语种
    toLang = 'zh'  # 译文语种
    salt = random.randint(32768, 65536)
    # 手动录入翻译内容，q存放
    sign = appid + q + str(salt) + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + \
            '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

    # 建立会话，返回结果
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)
        # response是HTTPResponse对象
        response = httpClient.getresponse()
        result_all = response.read().decode("utf-8")
        result = json.loads(result_all)
        trans_result = result['trans_result'][0]['dst']
    except Exception as e:
        print(e)
    finally:
        if httpClient:
            httpClient.close()
    return trans_result

if __name__ == '__main__':
    app = QApplication(sys.argv)
    show = MyWindow()
    show.show()
    sys.exit(app.exec_())



