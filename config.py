#!/usr/bin/env python
# -*- coding:utf-8 -*-

config = {}
doc_files = []
import chardet
def get_encoding(file):
    with open(file,'rb') as f:
        tmp = chardet.detect(f.read())
        return tmp['encoding']
encode = get_encoding("config.ini")
with open("config.ini", 'r', encoding=encode) as f:
    s = f.read()
    config = eval(s)

#     with open("config.ini", 'w', encoding="utf8") as fw:
#         fw.write(s)
# with open("config.ini", 'r', encoding="utf8") as f:
#     s = f.read()
#     config = eval(s)
#     # exec("config="+cr)
#     # config = eval(cr)
