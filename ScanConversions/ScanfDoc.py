#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :ScanfDoc.py
# @Time      :2021/8/9 11:35
# @Author    : 刘广鸿


from config import *
import os
from DocToDocx import docToDocx


class ScanFile:
    def __init__(self):
        self.len = None
        self.fileList = []

    def scanDocx(self):
        print("正在扫描文件列表...")
        for filename in os.listdir(config["filepath"]): # 将.doc => .docx
            print(filename)
            if filename.endswith('.doc'):
                docToDocx(filename, filename + "x")
                doc_files.append(config["filepath"]+"\\"+filename + "x")  # 记录doc结尾的文件
                # self.fileList.append(filename + "x")
        for filename in os.listdir(config["filepath"]):
            print(filename)
            if filename.endswith('.docx'):
                self.fileList.append(config["filepath"]+"\\"+filename)

        self.len = len(self.fileList)
        return self.fileList

    def getlen(self):
        return self.len


if __name__ == '__main__':
    scan = ScanFile()
    filelist = scan.scanDocx()
    print("当前文件夹docx文件个数:%s" % len(filelist))  # 文件个数
    for filename in filelist:
        print(filename)
        # para = Parser(filename)
        # poj = para.parse()
