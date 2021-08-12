#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :docTest.py
# @Time      :2021/8/10 12:16
# @Author    : 刘广鸿


import docx
import os
from config import *
# import sys
from win32com.client import Dispatch


def docToDocx(docPath, docxPath):
    '''将doc转存为docx'''
    word = Dispatch('Word.Application')
    # print(sys.path)
    pathPrefix = config["filepath"]+'\\'
    doc = word.Documents.Open(pathPrefix+docPath)
    doc.SaveAs(pathPrefix+docxPath, FileFormat=12)
    doc.Close()


