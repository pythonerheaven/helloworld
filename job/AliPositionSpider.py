#!/usr/bin/python
#coding:utf-8
# Python 3.6.1

import csv
import json
import numpy as np
import pandas as pd
import requests



import csv
import json
import numpy as np
import pandas as pd
import requests


# 定义函数：请求职位信息
def get_content(profession, url, pageIndex, pageSize):
    # 职位列表
    positions_list = []
    # 结果集
    result_list = []

    # 请求参数格式化
    #params = {"pageSize": pageSize, "pageIndex": pageIndex, "keyWord": 'IOT'}
    #paramsJson = json.dumps(params).encode(encoding='utf-8')

    paramStr = '?pageSize='+ str(pageSize) + '&pageIndex='+str(pageIndex) + '&keyWord=' + profession
    # 发送请求
    response = requests.post(url = url + paramStr)
    # 解析响应
    resultJson = json.loads(response.content)
    datasJson = json.loads(json.dumps(resultJson['returnValue']))
    positions_list = datasJson['datas']
    positions_list = json.loads(json.dumps(positions_list))

    for i, position in enumerate(positions_list):
        position = json.dumps(position)
        positionJson = json.loads(position)

        temp = []
        position_name = positionJson['name']
        position_class = positionJson['secondCategory']
        if position.find('workLocation') >= 0:
           work_palce = positionJson['workLocation']
        else:
           work_palce = ''
        recruit_num = positionJson['recruitNumber']
        position_description = json.loads(json.dumps(positionJson['description']).replace('<br/>',''))
        position_requirements = json.loads(json.dumps(positionJson['requirement']).replace('<br/>',''))

        temp.append(position_name)
        temp.append(position_class)
        temp.append(work_palce)
        temp.append(recruit_num)
        temp.append(position_description)
        temp.append(position_requirements)

        result_list.append(temp)

    return result_list



# 根据抓包阿里巴巴获取职位信息api的URL的特性，使用上述函数循环抓取前100页数据
source_url = 'https://job.alibaba.com/zhaopin/socialPositionList/doList.json'
profession = '产品经理'
data_array = []
for i in range(5):
   pageIndex = i + 1
   data = get_content(profession,source_url, pageIndex, 100)
   data_array.extend(data)

# 更改数组的栏目名称
datas = pd.DataFrame(data_array, columns=['职位名称', '职位类别', '工作地点','招聘人数','岗位描述','岗位要求'])

# 生成excel文件到本地
data = datas.to_excel('/Users/hujiabao/workspace_python/helloworld/job/' + profession + '.xls')



