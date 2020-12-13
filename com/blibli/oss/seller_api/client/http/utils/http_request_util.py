import uuid
import re
import pytz
import json
import hashlib
import urlparse
import hmac
import base64

from datetime import datetime

from com.blibli.oss.seller_api.client.http.models.constant import Constant


def create_request_parameters(mandatory_parameter, params=None):
    request_parameters = {
        Constant.REQUEST_ID: str(uuid.uuid4()),
        Constant.STORE_CODE: mandatory_parameter.store_code,
        Constant.USERNAME: mandatory_parameter.username,
        Constant.STORE_ID: Constant.BLIBLI_STORE_ID,
        Constant.CHANNEL_ID: re.sub(Constant.WHITESPACE_REGEX_KEY, Constant.DASH,
                                    mandatory_parameter.company_name).lower()
    }
    if params:
        request_parameters = request_parameters.update(params)
    return request_parameters


def create_request_headers(method, url, mandatory_headers, body=None):
    request_headers = {
        Constant.CONTENT_TYPE: Constant.APPLICATION_JSON_VALUE,
        Constant.ACCEPT: Constant.APPLICATION_JSON_VALUE,
        Constant.API_SELLER_KEY: mandatory_headers.api_seller_key
    }
    if mandatory_headers.signature_key:
        timezone = pytz.timezone(Constant.DEFAULT_TIMEZONE)
        signature_time = datetime.now(timezone)
        request_headers[Constant.SIGNATURE] = generate_signature(method, url,
                                                                 mandatory_headers.signature_key,
                                                                 signature_time, body)
        request_headers[Constant.SIGNATURE_TIME] = str(to_timestamp(signature_time))
    return request_headers


def generate_signature(method, url, signature_key, signature_time, body=None):
    signature_time = signature_time.strftime(Constant.SIGNATURE_TIME_FORMAT)
    if body:
        md5_body = hashlib.md5(json.dumps(body)).hexdigest()
        content_type = Constant.APPLICATION_JSON_VALUE
    else:
        md5_body = Constant.EMPTY
        content_type = Constant.EMPTY
    raw_signature = method + Constant.NEW_LINE + md5_body + Constant.NEW_LINE + \
                    content_type + Constant.NEW_LINE + signature_time + Constant.NEW_LINE + \
                    urlparse.urlparse(url).path
    signature = hmac.new(str(signature_key), msg=raw_signature, digestmod=hashlib.sha256) \
        .digest()
    return base64.b64encode(signature)


def to_timestamp(date):
    epoch = datetime(1970, 1, 1, tzinfo=pytz.timezone(Constant.DEFAULT_TIMEZONE))
    diff = date.astimezone(pytz.UTC) - epoch
    return int(diff.total_seconds())
