#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :MatchRule.py
# @Time      :2021/8/9 19:09
# @Author    : 刘广鸿

import re
from config import *

class MatchRule:
    """
        rule_Type ： 规则类型
        __matchFunction:  规则执行函数
    """

    def __init__(self, rule_Type: str = None, __matchFunction: classmethod = None):
        if __matchFunction is not None and not callable(__matchFunction):
            raise TypeError("the __matchFunction must be callable")
        self.__rule_Type = rule_Type  # 规则类型
        self.__matchFunction = __matchFunction  # 规则执行函数

    def Match(self, rules: str, src: str) -> list:
        try:
            ret = self.__matchFunction(rules, src)
            return ret
        except Exception as e:  # 如果规则 __matchFunction 为 None
            raise e

    def setRuleType(self, rule_Type: str):
        self.__rule_Type = rule_Type

    def getRuleType(self):
        return self.__rule_Type

    def setMatchFunction(self, __matchFunction: classmethod):
        if __matchFunction is not None and not callable(__matchFunction):
            raise TypeError("the __matchFunction must be callable")
        self.__matchFunction = __matchFunction

    def getMatchFunction(self):
        return self.__matchFunction


class ReMatchRule(MatchRule):

    def __init__(self, __matchFunction: classmethod = re.findall):
        super(ReMatchRule, self).__init__("reregular", __matchFunction)


if __name__ == '__main__':
    r1 = ReMatchRule()
    # r1.Match()
