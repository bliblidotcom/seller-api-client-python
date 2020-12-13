import requests

from com.blibli.oss.seller_api.client.http.models.Constant import Constant
from com.blibli.oss.seller_api.client.http.utils import HttpRequestUtil


def get(url, mandatory_parameter, mandatory_header, params=None, timeout=None):
    return request(Constant.HTTP_METHOD_GET, url, mandatory_parameter,
                   mandatory_header, params=params, timeout=timeout)


def post(url, mandatory_parameter, mandatory_header, body=None, params=None, timeout=None):
    return request(Constant.HTTP_METHOD_POST, url, mandatory_parameter,
                   mandatory_header, body=body, params=params, timeout=timeout)


def put(url, mandatory_parameter, mandatory_header, body=None, params=None, timeout=None):
    return request(Constant.HTTP_METHOD_PUT, url, mandatory_parameter,
                   mandatory_header, body=body, params=params, timeout=timeout)


def patch(url, mandatory_parameter, mandatory_header, body=None, params=None, timeout=None):
    return request(Constant.HTTP_METHOD_PATCH, url, mandatory_parameter,
                   mandatory_header, body=body, params=params, timeout=timeout)


def delete(url, mandatory_parameter, mandatory_header, params=None, timeout=None):
    return request(Constant.HTTP_METHOD_DELETE, url, mandatory_parameter,
                   mandatory_header, params=params, timeout=timeout)


def request(method, url, mandatory_parameter, mandatory_header, body=None, params=None, timeout=None):
    __validate_request(method, url, mandatory_parameter, mandatory_header)
    timeout = __get_default_timeout(timeout)
    params = HttpRequestUtil.create_request_parameters(mandatory_parameter, params)
    headers = HttpRequestUtil.create_request_headers(method, url, mandatory_header, body)
    auth = (mandatory_header.api_client_id, mandatory_header.api_client_key)
    return requests.request(method, url, data=body, params=params,
                            headers=headers, auth=auth, timeout=timeout)


def __get_default_timeout(timeout):
    if timeout is None:
        timeout = Constant.DEFAULT_TIMEOUT
    return timeout


def __validate_request(method, url, mandatory_parameter, mandatory_header):
    if not method:
        raise Exception("Need to pass request Method")
    if not url:
        raise Exception("Need to pass request Url")
    if mandatory_parameter is None:
        raise Exception("Need to pass Mandatory Parameter")
    if mandatory_header is None:
        raise Exception("Need to pass Mandatory Header")