class MandatoryHeader:
    def __init__(self, api_client_id, api_client_key, api_seller_key, signature_key=None):
        self.api_client_id = api_client_id
        self.api_client_key = api_client_key
        self.api_seller_key = api_seller_key
        self.signature_key = signature_key

    def set_signature_key(self, signature_key):
        self.signature_key = signature_key
