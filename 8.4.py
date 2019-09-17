import json
import csv
import numpy as np
def csv(path):
    with open(path,'r') as csvfile:
        reader = csv.reader(csvfile)
        list = []
        valuename = []
        for row in reader:
            list.append(row)     #将获取的数据全部放到list中
        for i in range(len(list)):
            key = list[0]        #将list中的第一条数据当作键名
            if i !=0:
                li = list[i]
                valuename.append(li)   #将其他数据当作键值放入valuename中
        value_ = np.array(valuename).T   #将列表转为数组并转置
        value = value_.tolist()
        test_dict = dict(zip(key,value))
        json_str = json.dumps(test_dict)
        with open("D:/DES/Weekhomework/js.json",'w') as json_file:
            json_file.write(json_str)
csv('D:/DES/Weekhomework/Hospita   