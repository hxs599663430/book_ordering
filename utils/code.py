class ResponseCode:
    Fail = -1   # 失败，未知错误
    Success = 200   # 成功
    ParamsError = 400     # 错误，参数错误
    NoResourceFound = 404   # 未找到资源


class ResponseMessage:
    FailMessage = "失败，未知错误"
    SuccessMessage = "执行操作成功"
    ParamsErrorMessage = "参数错误"
    NoResounceFoundMessage = "未找到资源"
