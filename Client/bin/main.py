# -*- coding: utf-8 -*-
# @Time    : 2018/6/11 8:51
# @Author  : Tianhao
# @Email   : xth9363@163.com
# @File    : main.py
# @Software: PyCharm

# 脚本解释器
# -*- coding:utf-8 -*-

'''
bin是客户端启动脚本的所在目录
conf是配置文件目录
core是核心代码目录
log是日志文件保存目录
plugins是插件或工具目录
'''
import os
import sys

BASE_DIR = os.path.dirname(os.getcwd())
# 设置工作目录，使得包和模块能够正常导入
sys.path.append(BASE_DIR)

from core import handler

if __name__ == '__main__':
    handler.ArgvHandler(sys.argv)
