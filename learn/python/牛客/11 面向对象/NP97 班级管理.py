#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : NP97 班级管理.py
@Author  : ChenLiRui
@Time    : 2024/7/26 下午4:36
@explain : 文件说明
"""


class Student:
    def __init__(self, name, student_id, score, homework_grades):
        self.name = name
        self.student_id = student_id
        self.score = score
        self.homework_grades = homework_grades

    def print_info(self):
        print(
            f"{self.name}'s student "
            f"number is {self.student_id}, "
            f"and his grade is {self.score}. "
            f"He submitted {len(self.homework_grades)}"
            f" assignments, each with a grade "
            f"of {' '.join(self.homework_grades)}"
        )


if __name__ == '__main__':
    name = input()
    student_id = input()
    score = int(input())
    homework_grades = input().split()

    student = Student(name, student_id, score, homework_grades)
    student.print_info()
    pass
