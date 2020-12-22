from ai_web.models import PmiLog
import random
from .file_parse import PmiParse
import json

class Uplaod_data():
    def __init__(self):
        self.string_id = 0
        self.i = []
        self.v = []

def insert(pmi_data):
    string_cnt = 0
    for iv_data in pmi_data.iv:
        string_cnt += 1
        for i in iv_data:
            datafiled = PmiLog()
            datafiled.log_id = 1
            datafiled.log_name = 'pmi_log'
            datafiled.string_id = string_cnt
            datafiled.current = i[0]
            datafiled.voltage = i[1]
            datafiled.save()

def find():
    result = PmiLog.objects.filter(log_id=1)
    encode_data = []
    data = []
    # for i in result:
    #     is_found = False
    #     for j in encode_data:
    #         if i.string_id in j.string_id:
    #             content = {'电压': i.voltage, '电流': i.current}
    #             j.iv.append(content)
    #             is_found = True
    #             break
    #     if is_found == False:
    #         k = Uplaod_data()
    #         k.string_id = i.string_id
    #         content = {'电压': i.voltage, '电流': i.current}
    #         k.iv.append(content)
    #         encode_data.append(k)

    # for j in encode_data:
    #     text = {"PV" + j.string_id:j.iv}
    #     data.append(text)
    k = Uplaod_data()
    k.string_id="pv1"
    k.i= [1,2,3,4,5,6,7]
    k.v= [9,1,2,3,4,5,6]    
    # return json.dumps(k, ensure_ascii=False)
    return k


def delete():
    PmiLog.objects.filter(log_id=1).delete()