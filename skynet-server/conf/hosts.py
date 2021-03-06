#!/usr/bin/env python
# coding: utf-8
__author__ = 'whoami'

"""
@version: 1.0
@author: whoami
@license: Apache Licence 2.0
@contact: skynetEye@gmail.com
@site: http://www.itweet.cn
@software: PyCharm Community Edition
@file: hosts.py
@time: 2015-11-26 下午8:34
"""

import templates

g1 = templates.LinuxTemplate()
g1.group_name = 'Linux Default Groups'
g1.hosts = ['127.0.0.1','127.0.1.1']

g2 = templates.NetworkTemplate()
g2.group_name = 'Linux Network Groups'
g2.hosts = ['127.0.0.1']

monitored_groups = [
    g1,g2
]

monitored_network_groups = [
    g2
]
