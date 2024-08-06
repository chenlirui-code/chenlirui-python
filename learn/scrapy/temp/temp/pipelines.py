# 在这里定义你的Item处理管道
#
# 不要忘记将管道添加到ITEM_PIPELINES设置中
# 参考：https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# 用于使用单一接口处理不同类型Item的模块
from itemadapter import ItemAdapter


class TempPipeline:
    def process_item(self, item, spider):
        return item
