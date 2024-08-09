# 在此定义您的项目管道
#
# 别忘了将您的管道添加到 ITEM_PIPELINES 设置中
# 参考：https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 对于使用单个接口处理不同的项目类型很有用
from itemadapter import ItemAdapter  # 导入相关模块


class TempPipeline:  # 定义名为 TempPipeline 的类
    def process_item(self, item, spider):  # 处理项目的方法
        return item  # 这里直接返回项目，未做具体处理
