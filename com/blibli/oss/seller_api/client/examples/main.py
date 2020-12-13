from com.blibli.oss.seller_api.client.http.core import http_request
from com.blibli.oss.seller_api.client.http.models.mandatory_parameter import MandatoryParameter
from com.blibli.oss.seller_api.client.http.models.mandatory_header import MandatoryHeader

if __name__ == "__main__":
    mandatory_parameter = MandatoryParameter("client.sdk@mailinator.com",
                                             "SDC-60001",
                                             "My Company")
    mandatory_header = MandatoryHeader("mta-api-clientsdk-cc80f",
                                       "mta-api-ySvFBOwPHTTBhccx89y2QxORSyFEesT55H2ws95fbPs8fsNV9y",
                                       "495930D13E51161331FB6423B048FB759B39E1573F90673F94558D727C04E917",
                                       "secret")
    params = {
        "orderNo": "40000198525",
        "orderItemNo": "40000262429"
    }
    order_detail_url = "https://api-uata.gdn-app.com/v2/proxy/mta/api/businesspartner/v1/order/orderDetail"
    response = http_request.get(order_detail_url, mandatory_parameter, mandatory_header, params, 10)
    print response
    print response.content