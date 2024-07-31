#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    : t.py
@Author  : ChenLiRui
@Time    : 2024/7/30 下午3:04
@explain : 文件说明
"""
from selenium import webdriver
import cv2
import random
import time


class SliderVerification:
    def __init__(self, driver):
        self.driver = driver

    def get_images(self):
        """第一步：得到验证码图片base64数据"""
        # 得到完整的图片base64数据,"return"必须加上
        full_js = "return document.getElementsByTagName('img')[0].src"
        full_image = self.driver.execute_script(full_js)
        # 得到缺口的图片base64数据
        gap_js = "return document.getElementsByTagName('img')[1].src"
        gap_image = self.driver.execute_script(gap_js)
        # 设置保存路径
        base_path = fun().uppath() + "/data/image"
        full_path = base_path + "/full_image.png"
        gap_path = base_path + "/gap_image.png"
        # 转换
        self.base64_to_image(full_image, full_path)
        self.base64_to_image(gap_image, gap_path)
        # 返回路径
        return full_path, gap_path

    def base64_to_image(self, base64_str, image_path=None):
        """在第一步里：base64转化为image"""
        base64_data = re.sub('^data:image/.+;base64,', '', base64_str)
        byte_data = base64.b64decode(base64_data)
        image_data = BytesIO(byte_data)
        img = Image.open(image_data)
        if image_path:
            img.save(image_path)
        return img

    def match_gaps(self, full, gap):
        """第二步：匹配缺口照片在完整照片的位置"""
        # 读取图片文件信息
        img_full = cv2.imread(full)
        template = cv2.imread(gap, 0)  # 以灰度模式加载图片

        # 使用 cv2.TM_CCOEFF_NORMED 方法进行匹配
        res = cv2.matchTemplate(img_full, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
        top_left = max_loc  # 匹配到的左上角位置

        return top_left[0]  # 返回 x 坐标

    def sliding_track(self, distance):
        """第三步：机器模拟人工滑动轨迹"""
        # 按住按钮
        self.driver.click_and_hold(loc.verify_button_loc)
        # 获取轨迹
        track = self.get_track(distance)
        print(f"获取轨迹：{track}")
        print("++++++++++++++++++++++++++++++++++++++++++++")
        for t in track:
            self.driver.move_by_offset(t)
            self.driver.move_by_offset(5)
            self.driver.move_by_offset(-5)
        # 松开按钮
        self.driver.release()

    def get_track(self, distance):
        """在第三步里：滑块移动轨迹"""
        track = []
        current = 0
        mid = distance * 3 / 4
        t = random.randint(5, 6) / 10
        v = 0

        while current < distance:
            if current < mid:
                a = 6
            else:
                a = -7
            v0 = v
            v = v0 + a * t
            move = v0 * t + 3 / 4 * a * t * t
            current += move
            track.append(round(move))

        return track

    def judgebox(self):
        """第四步：判断拼图是否存在"""
        box_js = "return document.getElementsByClassName('verifybox')"
        box_is = self.driver.execute_script(box_js)
        return len(box_is) > 0

    def loop(self):
        """第五步：滑块拼图递归循环调用"""
        # 得到验证码图片
        full_img_path, gap_img_path = self.get_images()
        # 匹配缺口照片在完整照片的位置
        number = self.match_gaps(full_img_path, gap_img_path)
        print(f"缺口照片的位置为：{number}")
        # 机器模拟人工滑动轨迹
        self.sliding_track(number)
        if self.judgebox():
            self.loop()


# 使用示例
driver = webdriver.Chrome()  # 请根据实际使用的浏览器进行初始化
verification = SliderVerification(driver)
verification.loop()
