#!/usr/bin/env python
# coding: utf-8
__author__ = 'whoami'

"""
@version: 1.0
@author: whoami
@license: Apache Licence 2.0
@contact: skynet@gmail.com
@site: http://www.itweet.cn
@software: PyCharm Community Edition
@file: SkynetAgentProtoImpl.py
@time: 2015-12-27 下午2:06
"""


import grpc
import skynet_core_pb2
import pickle
from SkynetLog import SkynetLog
import json
import os

log = SkynetLog(__file__).log()

class SkynetAgentProtoImpl(object):

    def __init__(self,master_ip,master_port):
        self.channel = grpc.insecure_channel('%s:%s' %(master_ip,master_port))
        self.stub = skynet_core_pb2.SkynetProtoStub(self.channel)

    def getConfigs(self,host_ip):
        try:
            response = self.stub.configs(skynet_core_pb2.call(request_msg=host_ip))
            return response.reply_msg
        except Exception,e:
            log.error('Connect to skynet server timeout.')

    def push(self,msg):
        try:
            if msg:
                response = self.stub.push(skynet_core_pb2.call(request_msg=msg))
                if response.reply_msg == 'success':
                    return True
            else:
                log.warn('Push data to skynet server fail,push centent cannot be empty.')
        except Exception,e:
            log.error('Connect to skynet server timeout.')
            return False

    def jobs(self,task):
        pass

    def register(self,reg_data):
        if reg_data:
            try:
                if os.path.exists('/opt/rrd_data/reg_id.json'):
                    pass
                else:
                    response = self.stub.register(skynet_core_pb2.call(request_msg=pickle.dumps(reg_data)))

                    if response.reply_msg == 'success':
                        try:
                            reg_json = open('/opt/rrd_data/reg_id.json','w')
                            json.dump(reg_data, reg_json)
                            log.info('Register to skynet server success.')
                        except IOError,e:
                            print e
                            log.error('Generate reg_id fail. %s' %e)
                        finally:
                            if reg_json is not None:
                                reg_json.close()
                    else:
                        log.error('Register to skynet server fail. %s' %response.reply_msg)

            except Exception,e:
                log.error(e)
        else:
            log.warn('Register centent can not be empty.')

if __name__ == '__main__':
    sap = SkynetAgentProtoImpl()
    print sap.getConfigs('HostConfig::127.0.0.1')