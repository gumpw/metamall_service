import json
import random
import re
from datetime import datetime
from string import Template

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import SmsType, SmsRecord, SmsTemplate, Config, Province, City, Area
from api.serializers import ConfigSerializer, SmsRequestSerializer, SmsTemplateSerializer, ProvinceSerializer, \
    CitySerializer, QuerySerializer, AreaSerializer
from service.json_util import parseRequest
from service.sms_service import send_sms


@api_view(["POST"])
def login(request):
    pass


@api_view(["POST"])
def register(request):
    pass


@api_view(["GET", "POST"])
def province(request):
    province_list = ProvinceSerializer(Province.objects.all(), many=True)
    return Response(province_list.data, status.HTTP_200_OK)


@api_view(["GET", "POST"])
def city(request):
    try:
        # print(type(request.data))
        # json_query = json.load(request.data.get('_content'))
        provinceId = request.GET.get("provinceId")
        city = CitySerializer(request.data)
        city_list = CitySerializer(City.objects.filter(provinceId=provinceId), many=True)
        return Response(city_list.data, status.HTTP_200_OK)
    except Exception as e:
        return Response({}, status.HTTP_404_NOT_FOUND)


@api_view(["GET", "POST"])
def area(request):
    try:
        cityId = request.GET.get("cityId")
        area_list = AreaSerializer(Area.objects.filter(cityId=cityId), many=True)
        return Response(area_list.data, status.HTTP_200_OK)
    except:
        return Response({}, status.HTTP_404_NOT_FOUND)


@api_view(["POST"])
def sms(request):
    """
    短信发送接口
    ---
    request_serializer: SmsRequestSerializer
    """
    try:
        smsRequest = SmsRequestSerializer(data=request.data)
        smsRequest.is_valid()
        mobileNo = smsRequest.data['phoneNo']
        type = smsRequest.data['type']
        smsType = SmsType.objects.get(type=type)
        assert smsType is not None
    except AssertionError:
        return Response({"code": "F", "msg": "短信请求用途不合法"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    pattern = re.compile('^0\d{2,3}\d{7,8}$|^1[358]\d{9}$|^147\d{8}$')
    match = pattern.match(mobileNo)
    if not match:
        return Response({"code": "F", "msg": "手机号码不合法"}, status=status.HTTP_406_NOT_ACCEPTABLE)
    code = generate_code()
    codeKey = type + "-code"
    request.session[codeKey] = str(code)
    arr = {"verifyCode": code}
    try:
        smsTemplate = SmsTemplate.objects.get(type=type)
        serializer = SmsTemplateSerializer(smsTemplate, many=False)
    except SmsTemplate.DoesNotExist:
        return Response({"code": "F", "msg": "短信模板未配置"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    template = Template(serializer.data['templateContent'])
    try:
        smsConfig = Config.objects.get(configName="smsConfig")
        configSerializer = ConfigSerializer(smsConfig, many=False)
        configContent = configSerializer.data['configContent']
        configJson = json.loads(configContent)
    except Config.DoesNotExist:
        return Response({"code": "F", "msg": "短信配置为空"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    except (ValueError, KeyError, TypeError):
        return Response({"code": "F", "msg": "短信配置解析出错"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    content = template.substitute(arr)
    # 短信发送记录
    smsRecord = SmsRecord(phoneNo=mobileNo, content=content, verifyCode=code, type=smsType, gmtCreate=datetime.now())
    smsRecord.save()
    result = send_sms(mobileNo, content, configJson['url'], configJson['api'])
    # TODO:返回结果吗仍需要处理
    return Response({"code": "S", "msg": "短信发送成功"}, status.HTTP_200_OK)


@api_view(["POST"])
def goods(request):
    pass


@api_view(["GET"])
def test(request):
    return Response({"code": "S", "msg": "test"}, status.HTTP_200_OK)


def generate_code():
    return random.randint(100000, 999999)
