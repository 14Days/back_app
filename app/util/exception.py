# 注册异常
class RegisterException(Exception):
    err_msg = None

    def __init__(self, err_msg):
        self.err_msg = err_msg

    def __str__(self):
        return self.err_msg


# 登录异常
class LoginException(Exception):
    err_msg = None

    def __init__(self, err_msg):
        self.err_msg = err_msg

    def __str__(self):
        return self.err_msg


# 数据库操作异常
class DataBaseException(Exception):
    err_msg = None

    def __init__(self, err_msg):
        self.err_msg = err_msg

    def __str__(self):
        return self.err_msg


# 一般异常
class CommonException(Exception):
    err_msg = None

    def __init__(self, err_msg):
        self.err_msg = err_msg

    def __str__(self):
        return self.err_msg
