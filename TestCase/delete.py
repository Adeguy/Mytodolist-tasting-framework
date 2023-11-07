from Horizon_framework import DataFormZephyrScale, Assertions, InterfaceTesting
from ENV.config import access_key,base_URL
# access_key、base_URL存环境变量
case_data = DataFormZephyrScale(access_key)  # 输入许可码
APItest = InterfaceTesting(base_URL)  # 输入根地址
# 从用例管理平台获取数据
data = case_data.data_form_zephyr_scale('HOR-T89')
# 对获得数据进行整理
data_handed = case_data.data_handling(data)
print(data_handed)
# 进行接口测试
response = APItest.send_post(
    endpoint=data_handed['endpoint'],

    data={
            data_handed["id_pre_head"]: data_handed['id_head'],
            data_handed['date_pre_head']: data_handed["date_head"],
            data_handed["priority_pre_head"]: data_handed["priority_head"],
            data_handed["content_pre_head"]:data_handed["content_head"]
        }
)
# 进行断言
Asser = Assertions(data_handed['状态码'])
print(Asser.is_equal(response.status_code))  # 这里返回的是true和false
