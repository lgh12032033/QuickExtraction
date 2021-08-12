#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :main.py
# @Time      :2021/8/9 13:19
# @Author    : 刘广鸿

from TableGeneration import *
import time
import os
import sys
from log import Log


def main():
    scan = ScanFile()
    filelist = scan.scanDocx()
    print("当前文件夹docx文件个数:%s" % len(filelist))  # 文件个数
    excel = TableGeneration(config["outputPath"])
    try:
        for filename in filelist:
            # print(filename)
            doc = docx.Document(filename)
            text = ""
            for para in doc.paragraphs:
                text += para.text
            # with open(filename[:-4]+"txt","w",encoding="utf8") as f:
            #     f.write(text)
            excel.writeProject(text, filename)
        excel.saveFile()
        for doc in doc_files:
            doc.replace("\\", "\\\\")

            os.remove(doc)
    except Exception as e:
        for doc in doc_files:
            doc.replace("\\", "\\\\")
            os.remove(doc)
        logger.exception(sys.exc_info())
    finally:
        # 返回或者记录结果
        logger.info('共耗时 {0} 秒'.format(time.time() - time_begin))

    # scan = ScanFile()
    # filelist = scan.scanDocx()
    # filelist_len = len(filelist)
    # print("当前文件夹docx文件个数:%s" % filelist_len)  # 文件个数
    # fileN = input("请给生成的excel表格命名:")
    # table = TableGeneration(fileN)
    # table.setTitle()
    # COUNT = 0
    # datetime = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime())
    # with open("%s log.txt" % datetime, 'w', encoding="utf8") as f:
    #     f.write("时间：%s\n" % datetime)
    #     f.write("docx文件个数：%d\n" % filelist_len)
    # for filename in filelist:
    #     try:
    #         print("正在解析第%d个docx文件" % (COUNT + 1))
    #         para = Parser(filename)
    #         poj = para.parse()
    #         table.writeProject(poj)
    #         filelist_len -= 1
    #         print("第%d个docx文件提取成功" % COUNT)
    #         print("剩余待提取文件个数：%d" % filelist_len)
    #         COUNT += 1
    #     except Exception as e:
    #         with open("%s log.txt" % datetime, "a+", encoding="utf8") as f:
    #             f.write("提取失败：%s\n" % filename)
    # with open("%s log.txt" % datetime, "a+", encoding="utf8") as f:
    #     f.write("提取成功个数：%d\n" % COUNT)
    # print("提取完成，成功提取文件：%d个" % COUNT)
    # table.saveFile()


if __name__ == '__main__':
    time_begin = time.time()
    logger = Log(os.path.basename(__file__)).set_logger()
    main()
