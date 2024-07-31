#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP99 修改属性2.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午4:48
@explain : 文件说明
"""


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def printclass(self):
        print(f"{self.name}'s salary is {self.salary}, and his age is {self.age}")


if __name__ == '__main__':
    name = input()
    salary = int(input())
    age = int(input())

    e = Employee(name, salary)

    print(hasattr(e, 'age'))

    if not hasattr(e, 'age'):
        setattr(e, 'age', age)

    e.printclass()
    pass
