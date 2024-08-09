#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : test.py
@Author  : ChenLiRui
@Time    : 2024/8/7 下午5:20
@explain : js代码示例
"""
import execjs

# 定义一段 JavaScript 代码
js_code = """
function multiply(a, b) {
    return a * b;
}
"""

# 创建一个执行环境
ctx = execjs.compile(js_code)

# 调用 JavaScript 函数并传递值
result = ctx.call('multiply', 5, 3)
print(result)
