from django.conf.urls import url
from . import views


app_name = 'logs'

urlpatterns = [
    url("log_info/", views.LogsView.as_view(), name="log_info"),    # 日志信息显示
]
