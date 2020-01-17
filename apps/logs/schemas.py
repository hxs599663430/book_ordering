import coreapi
import coreschema
from rest_framework.schemas import AutoSchema

token_field = coreapi.Field(
                name="Authorization",
                required=False,
                location="header",
                schema=coreschema.String(),
                description="格式：JWT 值",
        )
TokenSchema = AutoSchema([
                token_field
        ]
)

LogsSchema = AutoSchema([
    # token_field
    # 设置前台传的参数名称、约束选项、方式、传参类型、描述等
    coreapi.Field("log_id",
                  required=False,
                  location="query",
                  schema=coreschema.String(),
                  description="日志编号", ),
    coreapi.Field("name",
                  required=False,
                  location="query",
                  schema=coreschema.String(),
                  description="客户(员工)名称", ),
    coreapi.Field("runtime",
                  required=False,
                  location="query",
                  schema=coreschema.String(),
                  description="执行时间", ),
])

LogsOutputSchema = AutoSchema([
    coreapi.Field("startTime",
                  required=False,
                  location="query",
                  schema=coreschema.String(),
                  description="开始时间", ),
    coreapi.Field("endTime",
                  required=False,
                  location="query",
                  schema=coreschema.String(),
                  description="结束时间", ),
])
