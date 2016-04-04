#!/usr/bin/env python
# encoding: utf-8
"""
    @author: Magic Joey
    @contact: outlierw@gmail.com
    @site: http://underestimated.me
    @project: mystery
    @description:
    @version: 2016-01-03 00:38,parseUtil V1.0
"""
import json


def parseRequest(data):
    result = {}
    for kk in data.keys():
        result[kk] = data[kk]
    return result


class MtJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        return json.JSONEncoder.default(self, obj)


def func():
    pass


class Main():
    def __init__(self):
        pass


if __name__ == '__main__':
    pass
