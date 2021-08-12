#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :Project.py
# @Time      :2021/8/8 23:56
# @Author    : 刘广鸿

from MatchRule import *
import xlwt
import re


class Project:
    """
        这是一个  excel  规则匹配对象 可以根据不同的规则进行数据匹配
    @member:
        MatchRule:      匹配规则类型
            rules       匹配规则语句
            rule_Type   规则类型
        col_name    列名
        col         列数
        sheet       表对象
        row         默认递增不可设置
        lastfilled  上次填充内容
    """

    def __init__(self, match_Rule: MatchRule, column):
        if MatchRule is None or not isinstance(match_Rule, MatchRule):
            raise TypeError("match_Rule must be MatchRule")
        self.__MatchRule = match_Rule
        if not isinstance(column["col"], int):
            raise TypeError("col must be int")  # 列只能是整数
        # self.__col = col

        if not isinstance(column["cloumnName"], str):
            raise TypeError("col_name must be str")  # 列只能是字符串
        # self.__col_name = col_name
        self.__row = 0
        self.__column = column
        if "child" in self.__column:
            self.__child = self.__column["child"]
        else:
            self.__child = None

    def getCol(self):
        return self.__column["col"]

    def getRow(self):
        return self.__row

    def setColName(self, col_name: str, sheet):
        if not isinstance(col_name, str):
            raise TypeError("col_name must be str")  # 列只能是整数
        self.__col_name = col_name
        sheet.write(0, self.__column["col"], self.__column["name"])

    def setMatchRule(self, match_Rule: MatchRule):  # 修改规则
        if MatchRule is None or not isinstance(match_Rule, MatchRule):
            raise TypeError("match_Rule must be MatchRule")
        self.__MatchRule = MatchRule

    def init_colName(self, sheet):
        sheet.write(0, self.__column["col"], self.__column["cloumnName"])

    def getColumn(self):
        return self.__column

    def add_item(self, table, rule, text):
        self.__row += 1
        if self.__column["rule_Type"] == "reregular_noe":
            src = self.__MatchRule.Match(rule, text)
            # print("单匹配模式")
            if self.__child is not None:
                self.__row -= 1
                self.__child = self.__child
                if src is not None:
                    src = src[0]
                else:
                    src = ""
                self.traverse_child(table, src, self.__child)
                return
            if src is None or "":
                src = "未找到"
            else:
                src = src[0]  # 单匹配
        elif self.__column["Multiple"]:
            str_list = self.__MatchRule.Match(rule, text)  # 多匹配
            src = "、".join(str_list)
        elif not self.__column["Multiple"]:
            if self.__child is None:
                self.__row -= 1
                for item in self.__MatchRule.Match(rule, text):
                    self.__row += 1
                    table.work_sheet.write(self.__row, self.__column["col"], item)
                    self.lastFill = item  # 记录上次填充
                    for column in table.cols:
                        if column != self:
                            self.fillSameLine(table, self.__row, column)
                        elif column == self:
                            break
            else:
                self.__row -= 1
                for childtext in self.__MatchRule.Match(rule, text):
                    self.traverse_child(table, childtext, self.__child)
            return
        table.work_sheet.write(self.__row, self.__column["col"], src)
        self.lastFill = src  # 记录上次填充

    def traverse_child(self, table, childtext, child):
        if child["rule_Type"] == "reregular_noe":
            if "child" in child:
                if re.search(child["lists_rule"], childtext) is not None or "":
                    src = re.search(child["lists_rule"], childtext)[0]
                else:
                    src = ""
                self.traverse_child(table, src, child["child"])
            if re.search(child["lists_rule"], childtext) is None:
                src = "未找到"
            else:
                src = re.search(child["lists_rule"], childtext)[0]
            self.__row += 1
            table.work_sheet.write(self.__row, self.__column["col"], src)
            self.lastFill = src  # 记录上次填充
            for column in table.cols:
                if column != self:
                    self.fillSameLine(table, self.__row, column)
                elif column == self:
                    break

        elif child["rule_Type"] == "reregular":
            str_list = re.findall(child["lists_rule"], childtext)
            if child["Multiple"]:
                src = "、".join(str_list)
                self.__row += 1
                table.work_sheet.write(self.__row, self.__column["col"], src)
                self.lastFill = src  # 记录上次填充
                for column in table.cols:
                    if column != self:
                        self.fillSameLine(table, self.__row, column)
                    elif column == self:
                        break

            elif not child["Multiple"]:
                if "child" in child:
                    for childtext in str_list:
                        self.traverse_child(table, childtext, child["child"])
                else:
                    for childtext in str_list:
                        self.__row += 1
                        table.work_sheet.write(self.__row, self.__column["col"], childtext)
                        self.lastFill = childtext  # 记录上次填充
                        for column in table.cols:
                            if column != self:
                                self.fillSameLine(table, self.__row, column)
                            elif column == self:
                                break

    def fillSameLine(self, table, row, column):
        if column.getRow() < row:
            column.addRow()
            table.work_sheet.write(column.getRow(), column.getCol(), column.lastFill)
        else:
            return

    def addRow(self):
        self.__row += 1
