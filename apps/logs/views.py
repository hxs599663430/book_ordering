from rest_framework import generics

from logs.models import Logs
from logs.schemas import LogsSchema
from logs.serializers import LogsSerializer


class LogsView(generics.ListAPIView):
    """
        日志信息: 条件可选
        #### 参数说明
        |字段名称|描述|必须|类型|
        |--|--|--|--|
        |page|分页|False|int|
        |log_id|日志编号|False|string|
        |name|客户(员工)名称|False|string|
        |runtime|执行时间|False|datetime|

        #### 响应字段说明
        |字段名称|描述|必须|类型|
        |--|--|--|--|
        |id|日志记录id|--|int|
        |log_id|日志编号|--|string|
        |name|客户(员工)名称|--|string|
        |somethings|执行事件|--|string|
        |runtime|执行时间|--|string|

        #### 注意说明
        - 1 记录的所有信息。

        #### 响应消息：
        |Http响应码|原因|响应模型|
        |--|--|--|
        |200|请求成功|状态声明|
        |400|请求失败|参数错误|
    """
    queryset = Logs.objects.all()
    serializer_class = LogsSerializer
    schema = LogsSchema

    def get_queryset(self):
        log_id = self.request.query_params.get("log_id")
        name = self.request.query_params.get("name")
        runtime = self.request.query_params.get("runtime")

        query_obj = Logs.objects.all()
        if log_id:
            query_obj = Logs.objects.filter(log_id=log_id)
        if name:
            query_obj = query_obj.filter(name=name)
        if runtime:
            query_obj = query_obj.filter(runtime=runtime)

        if query_obj:
            return query_obj
        else:
            return self.queryset
