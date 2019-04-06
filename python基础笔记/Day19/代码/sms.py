# -*- coding: utf-8 -*-
import random
import sys
import uuid
from aliyunsdkdysmsapi.request.v20170525 import SendSmsRequest
from aliyunsdkdysmsapi.request.v20170525 import QuerySendDetailsRequest
from aliyunsdkcore.client import AcsClient
import uuid
from aliyunsdkcore.profile import region_provider
from aliyunsdkcore.http import method_type as MT
from aliyunsdkcore.http import format_type as FT
import const

try:
    reload(sys)
    sys.setdefaultencoding('utf8')
except NameError:
    pass
except Exception as err:
    raise err

# 注意：不要更改
REGION = "cn-hangzhou"
PRODUCT_NAME = "Dysmsapi"
DOMAIN = "dysmsapi.aliyuncs.com"

acs_client = AcsClient(const.ACCESS_KEY_ID, const.ACCESS_KEY_SECRET, REGION)
region_provider.add_endpoint(PRODUCT_NAME, REGION, DOMAIN)


class SMS:
    def __init__(self,signName,templateCode):
        self.signName = signName    # 签名
        self.templateCode = templateCode    # 模板code
        self.businessID = uuid.uuid1()
    def send(self,phone,para):
        smsRequest = SendSmsRequest.SendSmsRequest()
        # 申请的短信模板编码,必填
        smsRequest.set_TemplateCode(self.templateCode)

        # 短信模板变量参数
        if para is not None:
            smsRequest.set_TemplateParam(para)

        # 设置业务请求流水号，必填。
        smsRequest.set_OutId(self.businessID)

        # 短信签名
        smsRequest.set_SignName(self.signName)

        # 数据提交方式
        # smsRequest.set_method(MT.POST)

        # 数据提交格式
        # smsRequest.set_accept_format(FT.JSON)

        # 短信发送的号码列表，必填。
        smsRequest.set_PhoneNumbers(phone)

        # 调用短信发送接口，返回json
        smsResponse = acs_client.do_action_with_exception(smsRequest)
        # TODO 业务处理
        return smsResponse

if __name__ == "__main__":
    sms = SMS("lizhenguo123","SMS_161570285")
    phone = input("手机号：")
    para = random.randint(10000,99999)
    params = "{'code':'%d'}"%para



