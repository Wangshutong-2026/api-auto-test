import requests
import responses_validator
from commons.extract_utils import extract
import logging

logger = logging.getLogger('shutong')

def runner(k,v,my_var):

    match k:
        case 'request':  #发送请求
            logger.info('1.正在发送请求...')
            logger.info(f'{v}')
            my_var['resp'] = requests.request(**v)  #字典用**
        case 'response':  #断言响应
            logger.info('2.正在断言响应...')
            logger.info(f'{v}')
            responses_validator.validator(my_var['resp'], **v)  #字典用**
        case 'extract':  #变量提取
            logger.info('3.正在提取变量...')
            for var_name,var_exp in v.items():
                value = extract(my_var['resp'],*var_exp)  #列表用*
                logger.info(f'{var_name} = {value}')
        #查询数据库...

