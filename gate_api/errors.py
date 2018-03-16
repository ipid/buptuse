__all__ = ['GatewayApiError', 'GatewayNotLoginError', 'GatewayAlreadyLoginError']

class GatewayApiError(RuntimeError):
    def __init__(self, msg):
        super().__init__(msg)

class GatewayNotLoginError(GatewayApiError):
    def __init__(self):
        super().__init__("You are not logged in.")

class GatewayAlreadyLoginError(GatewayApiError):
    pass
