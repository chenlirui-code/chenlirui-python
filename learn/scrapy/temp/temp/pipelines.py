# �ڴ˶���������Ŀ�ܵ�
#
# �����˽����Ĺܵ���ӵ� ITEM_PIPELINES ������
# �ο���https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# ����ʹ�õ����ӿڴ���ͬ����Ŀ���ͺ�����
from itemadapter import ItemAdapter  # �������ģ��


class TempPipeline:  # ������Ϊ TempPipeline ����
    def process_item(self, item, spider):  # ������Ŀ�ķ���
        return item  # ����ֱ�ӷ�����Ŀ��δ�����崦��
