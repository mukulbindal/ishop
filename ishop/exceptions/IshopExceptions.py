class NoDataFoundError(Exception):
    def __init__(self, msg="No Data Found for requested item"):
        self.status = 404
        self.msg = msg
        super().__init__(self.msg)


class InsufficientStockError(Exception):
    def __init__(self, msg="Insufficient stock"):
        self.status = 404
        self.msg = msg
        super().__init__(self.msg)
