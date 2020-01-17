from rest_framework.response import Response

from utils.code import ResponseCode, ResponseMessage


class Results:

    @staticmethod
    def response_result(results):
        res_dict = {
            "code": ResponseCode.Success,
            "message": ResponseMessage.SuccessMessage,
            "results": results
        }
        return Response(res_dict)

    @staticmethod
    def response_success():
        res_dict = {
            "code": ResponseCode.Success,
            "message": ResponseMessage.SuccessMessage
        }
        return Response(res_dict)

    @staticmethod
    def response_params_error():
        res_dict = {
            "code": ResponseCode.ParamsError,
            "message": ResponseMessage.ParamsErrorMessage
        }
        return Response(res_dict)

    @staticmethod
    def response_fail():
        res_dict = {
            "code": ResponseCode.Fail,
            "message": ResponseMessage.FailMessage
        }
        return Response(res_dict)
