# -*- coding: utf-8 -*-
"""
    Exception
    ~~~~
    def of web exceptions

    :copyright: (c) 2017 by Baidu, Inc.
    :license: Apache, see LICENSE for more details.
"""


class DataNotFoundException(BaseException):
    """
    data not found
    """
    pass


class UnprocessableException(BaseException):
    """
    request param is unprocessable
    """
    pass
