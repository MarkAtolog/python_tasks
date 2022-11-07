import requests

from framework.api.response import Response
from framework.common.base_model import BaseModel
from framework.logger.logger import Logger


class ApiUtil:
    @staticmethod
    def get(url: str, params: dict = None, model: BaseModel | None = None):
        Logger().logger.info("Preparing GET request")
        req = requests.Request(method="GET",
                               url=url,
                               params=params).prepare()
        return ApiUtil.__send_request(req, model)

    @staticmethod
    def post(url: str,
             params: dict = None,
             data: object = None,
             model: BaseModel = None):
        Logger().logger.info("Preparing POST request")
        req = requests.Request(method="POST",
                               url=url,
                               params=params,
                               json=data.to_json()).prepare()
        return ApiUtil.__send_request(req, model)

    @staticmethod
    def delete(url: str, params: dict = None):
        Logger().logger.info("Preparing DELETE request")
        req = requests.Request(method="DELETE",
                               url=url,
                               params=params).prepare()
        return ApiUtil.__send_request(req)

    @staticmethod
    def put(url: str, params: dict = None, data: object = None):
        Logger().logger.info("Preparing PUT request")
        req = requests.Request(method="PUT",
                               url=url,
                               params=params,
                               data=data).prepare()
        return ApiUtil.__send_request(req)

    @staticmethod
    def __send_request(request,
                       model: BaseModel | None = None,
                       ) -> Response:
        Logger().logger.info(f"Sending prepared {request.method} request. Url = '{request.url}'")
        response = requests.session().send(request)
        Logger().logger.info(f"Response status code is {response.status_code}: {response.reason}")

        Logger().logger.info("Returning custom response object")
        return Response(
            status_code=response.status_code,
            content=response.text,
            headers=response.headers,
            model=model.create_from_dict(response.json()) if model is not None else None
        )
