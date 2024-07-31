import fitz
import os
import re

from paddleocr import PaddleOCR


def extract_pics(file_path, save_path):
    '''提取PDF中的所有图片'''
    result = []
    # 1.打开文件
    doc = fitz.open(file_path)
    # 文档页数
    page_count = len(doc)
    # print("文档共有{}页".format(page_count))
    # 2.遍历并检查每页的图片
    image_count = 0
    for i in range(page_count):
        # 页面对象
        page = doc[i]
        # 获取图片列表
        images = page.get_images()
        # 遍历图片
        for image in images:
            # 返回图片引用
            xref = image[0]
            # 根据引用从pdf中释放出图片
            base_image = doc.extract_image(xref)
            # 获得图片数据
            image_data = base_image["image"]
            # 保存图片
            if not os.path.exists(save_path):
                os.makedirs(save_path)
            cur_save_path = f'{save_path}/image_{image_count}.png'
            with open(cur_save_path, 'wb') as f:
                f.write(image_data)
                image_count = image_count + 1
            result.append(cur_save_path)
    # 3.关闭打开的pdf
    doc.close()
    return result


def extract_text(path):
    '''从图片中提取文字'''
    result_str = []
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')  # 只需要运行一次以将模型加载到内存中
    image_path = path
    result = ocr.ocr(image_path, cls=True)

    if result and result[0]:  # 如果结果非空且第一个元素非空
        for line in result[0]:
            result_str.append(str(line[1][0]))

    return result_str


def extract_code_one(text):
    '''处理文字的药品批准文号国药准字'''
    # 提取大写字母+8个数字的格式
    pattern1 = r'[A-Z]\d{8}'
    match1 = re.search(pattern1, text)
    if match1:
        return match1.group()
    return "识别失败"


def extract_code_two(text):
    '''处理文字的药品批准文号有效期'''
    # 尝试匹配4个数字+“-”+2个数字+“-”+2个数字的格式，最后一个数字可能是一个数字
    pattern1 = r'\d{4}-\d{2}-\d{1,2}'
    match1 = re.search(pattern1, text)
    if match1:
        return match1.group()

    # 尝试匹配4个数字+“年”+2个数字+“月”+2个数字+“日”的格式
    pattern2 = r'\d{4}年\d{2}月\d{2}日'
    match2 = re.search(pattern2, text)
    if match2:
        return match2.group()

    # 如果两种格式都没有匹配成功，返回识别失败
    return "识别失败"


def extract_result(file_list):
    '''从图片列表中提取需求文字'''
    av_str = None
    for x in file_list:
        # print('当前文件FileName:', x)
        str_list = extract_text(x)
        if "药品再注册批件" in str_list:
            # print(str_list)

            # 将str_list转换为字符串
            str_content = ''.join(str_list)
            # print(str_content)

            # 获取 审批结论 和 附件 之间的字段
            start_index = str_content.find('审批结论') + len('审批结论')
            end_index = str_content.find('附件')
            if 4 < start_index < end_index:
                str_content = str_content[start_index:end_index]
                # print(str_content)

                # 获取药品批准文号和药品批准文号有效期之间的字段
                av_str = extract_code_one(str_content)
                vate_str = extract_code_two(str_content)
            else:
                av_str = "识别失败"
                vate_str = "识别失败"

            # print(av_str)
            # print(vate_str)

            # 将这两个字段存在一个列表中
            return av_str, vate_str
    return None


def i_main(pdf_file_path, save_path):
    '''
    主函数
    :return:tuple(国药准字,国药准字有效期)
    '''
    file_list = extract_pics(pdf_file_path, save_path)
    # print("导出 {} 张图片".format(len(file_list)))
    result = extract_result(file_list)
    return result
