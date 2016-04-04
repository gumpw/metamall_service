#!/usr/bin/env python
# encoding: utf-8
"""
    @author: Magic Joey
    @contact: outlierw@gmail.com
    @site: http://underestimated.me
    @project: mystery
    @description:
    @version: 2016-01-02 22:46,sms V1.0
"""
import json
import requests


def send_sms(mobile_no, content, url, api):
    resp = requests.post(url,
                         auth=("api", "key-"+api),
                         data={
                             "mobile": mobile_no,
                             "message": content
                         }, timeout=3, verify=False)
    result = json.loads(resp.content.decode())
    return result


if __name__ == '__main__':
    utf8bytes = "卧槽".encode("utf-8")
    print(utf8bytes.decode())
    pass