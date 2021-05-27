#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
	功能：利用云开发http api操作小程序云数据库
'''



import requests
import json

APP_ID = 'wx9724d19532958326'
APP_SECRET = '0aa698618f7e004b4aa908da6292dab0'
ENV = 'cloud1-1gsabdsx6a087c46'
WECHAT_URL = "https://api.weixin.qq.com/"


def get_access_token():
    url = '{0}cgi-bin/token?grant_type=client_credential&appid={1}&secret={2}'.format(WECHAT_URL, APP_ID, APP_SECRET)
    response = requests.get(url)
    result = response.json()
    print(result)
    return result['access_token']


def get_upload_url(token, env, path):
    post_url = "https://api.weixin.qq.com/tcb/uploadfile?access_token=" + token
    playload = json.dumps({"env": env, "path": path})
    upload = requests.post(post_url, data=playload)
    return upload.json()


def get_download_url(token, env, file, time):
    playload = {}
    playload["env"] = env
    playload["file_list"] = []
    for item in file:
        file_dic = {}
        file_dic["fileid"] = item
        file_dic["max_age"] = time
        playload["file_list"].append(file_dic)
    post_url = "https://api.weixin.qq.com/tcb/batchdownloadfile?access_token=" + token
    print("playload:", playload)
    download = requests.post(post_url, data=json.dumps(playload))
    print("download", download)
    return download.json()


def parse_form(res):
    form = {}
    form["key"] = res["url"].split("/")[-1]
    form["Signature"] = res["authorization"]
    form["x-cos-security-token"] = res["token"]
    form["x-cos-meta-fileid"] = res["cos_file_id"]
    return form, res["url"]


def upload(res, file):
    form = res[0]
    upload_url = res[1]
    with open(file, "rb") as f:
        form["file"] = f.read()
        success = requests.post(upload_url, files=form)


def download(res, file):
    for i in range(len(res["file_list"])):
        download_url = res["file_list"][i]["download_url"]
        f = requests.get(download_url)
        with open(file[i], "wb") as code:
            code.write(f.content)



if __name__ == '__main__':
    TIME = 7200
    PATH = r"C:\Users\leahhh\Desktop\58a5d4bc4d3d400e7ecdf621ce023496.jpeg"
    PATH_ = [r"C:\Users\leahhh\Desktop\4.jpeg"]
    lst = ['cloud://cloud1-1gsabdsx6a087c46.636c-cloud1-1gsabdsx6a087c46-1305863916/58a5d4bc4d3d400e7ecdf621ce023496.jpeg']
    accessToken = get_access_token()
    RES = get_download_url(accessToken, ENV, lst, TIME)
    print(RES)
    download(RES, PATH_)
    # RES = get_upload_url(accessToken, ENV, PATH)
    # RES = parse_form(RES)
    # upload(RES, PATH)

# nohup python -u /data/szc/xly/generation/model/CommonsenseStoryGen/src/main.py --is_train 0 --cond 1 --model_dir /data/szc/xly/generation/model/models/117M --data_name roc --gpu 2 --data_dir /data/szc/xly/generation/model/CommonsenseStoryGen/data > /data/szc/xly/generation/model/CommonsenseStoryGen/log/4.log 2>&1 &
# nohup python -u /data/szc/xly/generation/model/CommonsenseStoryGen/src/main.py --is_train 1 --data_name multi_roc --model_dir /data/szc/xly/generation/model/models/117M --gpu 1 --data_dir /data/szc/xly/generation/model/CommonsenseStoryGen/data > /data/szc/xly/generation/model/CommonsenseStoryGen/log/3.log 2>&1 &


#
#
# import requests
# import json
# # import config
#
#
# # APP_ID = config.WECHAT_APP_ID
# APP_ID = 'wx9724d19532958326'
# # APP_SECRET = config.WECHAT_APP_SECRET
# APP_SECRET = '0aa698618f7e004b4aa908da6292dab0'
# # ENV = config.WECHAT_ENV  # 数据库环境id
# ENV = 'cloud1-1gsabdsx6a087c46'
# # TEST_COLLECTION = "test_collection"  # 数据库名称
# DB_NAME = "test"  # 数据库名称
#
# HEADER = {'content-type': 'application/json'}
# WECHAT_URL = "https://api.weixin.qq.com/"
#
#
# query_1 = '''
#     db.collection("test").add({
#         data:{
#             building:"博远楼",
#             date:"周一",
#             id_building:1,
#             id_date:1,
#             id_number:10,
#             id_room:1,
#             id_time:0,
#             room:"101"
#         }
#     })
# '''
# query_2 = '''
#     db.collection('test')
#     .where({id_building: 1, id_date: 1, id_room: 2, id_time: 0})
#     .get()
#     '''
# query_3 = '''
#     db.collection("test").add({
#         data:{
#             building:"博远楼",
#             date:"周一",
#             id_building:1,
#             id_date:1,
#             id_number:40,
#             id_room:2,
#             id_time:0,
#             room:"201"
#         }
#     })
# '''
#
#
# '''
# 获取小程序token
# '''
# def get_access_token():
#     url = '{0}cgi-bin/token?grant_type=client_credential&appid={1}&secret={2}'.format(WECHAT_URL, APP_ID, APP_SECRET)
#     response = requests.get(url)
#     result = response.json()
#     print(result)
#     return result['access_token']
#
#
# '''
# 新增集合
# '''
# def add_collection(accessToken):
#     url = '{0}tcb/databasecollectionadd?access_token={1}'.format(WECHAT_URL, accessToken)
#     data = {
#         "env": ENV,
#         "collection_name": DB_NAME
#     }
#     response = requests.post(url, data=json.dumps(data), headers=HEADER)
#     print('1.新增集合：' + response.text)
#
#
# '''
# 新增数据
# '''
# def add_data(accessToken, query):
#     url = '{0}tcb/databaseadd?access_token={1}'.format(WECHAT_URL, accessToken)
#     # query = '''
#     # db.collection(DB_NAME).add({
#     #     data:{
#     #         key:1,
#     #         value:"2345"
#     #     }
#     # })
#     # '''
#     # query = '''
#     # db.collection("test").add({
#     #     data:{
#     #         building:"博远楼",
#     #         date:"周一",
#     #         id_building:1,
#     #         id_date:1,
#     #         id_number:30,
#     #         id_room:3,
#     #         id_time:0,
#     #         room:"301"
#     #     }
#     # })
#     # '''
#     data = {
#         "env": ENV,
#         "query": query
#     }
#     response = requests.post(url, data=json.dumps(data), headers=HEADER)
#     print('2.新增数据：' + response.text)
#
#
# '''
# 查询数据
# '''
# def query_data(accessToken, query):
#     url = '{0}tcb/databasequery?access_token={1}'.format(WECHAT_URL, accessToken)
#     # query = '''
#     # db.collection('test').limit(10).skip(1).get()
#     # '''
#     # query = '''
#     #     db.collection('test')
#     #     .where({id_building: 1, id_date: 1, id_room: 2, id_time: 0})
#     #     .get()
#     #     '''
#     data = {
#         "env": ENV,
#         "query": query
#     }
#     response = requests.post(url, data=json.dumps(data), headers=HEADER)
#     if not response.json()['data']:
#         print('3.查询数据：查询失败')
#         return None
#     print('3.查询数据：' + response.text)
#     result = response.json()
#     resultValue = json.loads(result['data'][0])
#     print('人数：', resultValue['id_number'])
#     return resultValue['_id']
#
#
# '''
# 删除数据
# '''
# def delete_data(accessToken, id):
#     url = '{0}tcb/databasedelete?access_token={1}'.format(WECHAT_URL, accessToken)
#     query = '''db.collection('test').doc("{0}").remove()'''.format(id)
#     data = {
#         "env": ENV,
#         "query": query
#     }
#     response = requests.post(url, data=json.dumps(data), headers=HEADER)
#     print('4.删除数据：' + response.text)
#
#
# '''
# 修改数据
# '''
# def change_data(accessToken, query_a, query_b):
#     print('————————修改开始————————')
#     id = query_data(accessToken, query_a)
#     delete_data(accessToken, id)
#     add_data(accessToken, query_b)
#     print('5.修改数据：' + id)
#     print('————————修改结束————————')
#
#
# '''
# 删除集合
# '''
# def delete_collection(accessToken):
#     url = '{0}tcb/databasecollectiondelete?access_token={1}'.format(WECHAT_URL, accessToken)
#     data = {
#         "env": ENV,
#         "collection_name": DB_NAME
#     }
#     response = requests.post(url, data=json.dumps(data), headers=HEADER)
#     print('6.删除集合：' + response.text)
#
#
# if __name__ == '__main__':
#     # 0.获取token
#     accessToken = get_access_token()
#     # # 1.新增集合：
#     # add_collection(accessToken)
#     # # 2.新增数据
#     # add_data(accessToken, query_1)
#     # # 3.查询数据
#     # id_1 = query_data(accessToken, query_2)
#     # # 4.删除数据
#     # delete_data(accessToken, id_1)
#     # 5.修改数据
#     change_data(accessToken, query_2, query_3)
#     # 3.查询数据
#     id_2 = query_data(accessToken, query_2)
#     # # 6.删除集合
#     # delete_collection(accessToken)
#
