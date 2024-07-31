#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : sign.py
@Author  : ChenLiRui
@Time    : 2024/7/28 下午12:50
@explain : 文件说明
"""

# e: "asdjnjfenknafdfsdfsd"
# t: undefined
# const o = (new Date).getTime();
# sign: S(o, e),
# function _(e) {
#     return i.createHash("md5").update(e.toString()).digest("hex")
# }
# client mysticTime[:-1] product
# function S(e, t) {
#     return `client=${d}&mysticTime=${e}&product=${u}&key=${t}`
# }
import hashlib

def sa(e):
    m = hashlib.md5()
    m.update(e.encode())
    return m.hexdigest()


def S(e, t):
    return _(f"client=fanyideskweb&mysticTime={e}&product=webfanyi&key={t}")


if __name__ == '__main__':
    # 'client=fanyideskweb&mysticTime=asdjnjfenknafdfsdfsd&product=webfanyi&key="asdjnjfenknafdfsdfsd"'
    msg = 'client=fanyideskweb&mysticTime=1722155173079&product=webfanyi&key=asdjnjfenknafdfsdfsd'
    print(sa(msg))
    pass
