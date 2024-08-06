#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP98 修改属性1.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午4:42
@explain : 文件说明
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printclass(self):
        try:
            print(f"{self.name}'s salary is {self.salary}, and his age is {self.age}")
        except AttributeError:
            print("Error! No age")


if __name__ == '__main__':
    name = input()
    salary = int(input())
    e = Employee(name, salary)
    e.printclass()

    age = int(input())
    e.age = age
    e.printclass()
    pass
