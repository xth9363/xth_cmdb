# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 9:34
# @Author  : Tianhao
# @Email   : xth9363@163.com
# @File    : settings.py
# @Software: PyCharm


# -*- coding:utf-8 -*-

import os

# 远端服务器配置
# Params = {
#     "server": "127.0.0.1",
#     "port": 8000,
#     'url': '/assets/report/',
#     'request_timeout': 30,
# }
Params = {
    "server": "cmdb.xiatianhao.com",
    "port": 80,
    'url': '/assets/report/',
    'request_timeout': 30,
}

# 日志文件配置

PATH = os.path.join(os.path.dirname(os.getcwd()), 'log', 'cmdb.log')