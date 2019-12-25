import random
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from flask import current_app
from json import loads
from app.util.exception import RegisterException
from app.util.redis import red


def create_random_code() -> str:
    code = ''
    for i in range(0, 4):
        code += str(random.randint(1, 9))
    current_app.logger.info('create code %s', code)
    return code


def send_message(phone: str, code: str):
    client = AcsClient('LTAI4FhGUEeAihfxAc6BfvLX', 'Jv1nyFsHDHlf7YjgD76Qi7UdwNt8ZE', 'cn-hangzhou')

    request = CommonRequest()
    request.set_accept_format('json')
    request.set_domain('dysmsapi.aliyuncs.com')
    request.set_method('POST')
    request.set_protocol_type('https')  # https | http
    request.set_version('2017-05-25')
    request.set_action_name('SendSms')

    request.add_query_param('RegionId', "cn-hangzhou")
    request.add_query_param('PhoneNumbers', phone)
    request.add_query_param('SignName', "锦权家居")
    request.add_query_param('TemplateCode', "SMS_176939751")
    request.add_query_param('TemplateParam', "{\"code\": %s}" % code)

    response = loads(client.do_action_with_exception(request))
    if response['Code'] != 'OK':
        raise RegisterException(response['Message'])


def store_code_in_redis(phone: str, code: str):
    try:
        red.connection.set(phone, code)
        red.connection.expire(phone, 5 * 60)
    except ConnectionError:
        current_app.logger.info('failed in redis')
        raise


def get_code_from_redis(phone: str) -> bytes:
    code = red.connection.get(phone)
    return code
