import os
import sys
import urllib.request
import json
from pprint import pprint

file_path = 'C:\\Users\\Administrator\\yourStock\\test.txt'
labels = open(file_path).read().splitlines()

client_id = labels[0]
client_secret = labels[1]

print(client_id, client_secret)


def ToEn(koText):
    encText = urllib.parse.quote(koText)
    data = "source=ko&target=en&text=" + encText
    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)

    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        d = json.loads(result)
        print('--- korean to English ---')
        print('번역전:', koText)
        print('번역후', d['message']['result']['translatedText'])

    else:
        print("Error Code:" + rescode)


def ToKo(egText):
    kocText = urllib.parse.quote(egText)

    data = "source=en&target=ko&text=" + kocText

    url = "https://openapi.naver.com/v1/papago/n2mt"

    request = urllib.request.Request(url)

    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request, data=data.encode("utf-8"))
    rescode = response.getcode()
    if (rescode == 200):
        response_body = response.read()
        result = response_body.decode('utf-8')
        d = json.loads(result)
        print('--- English to Korean ---')
        print('번역전:', egText)
        print('번역후', d['message']['result']['translatedText'])

    else:
        print("Error Code:" + rescode)


ToEn('오늘부터 블로그를 시작 합니다')
ToKo('this is the last post in an overview series')
