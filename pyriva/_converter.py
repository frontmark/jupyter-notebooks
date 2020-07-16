# -*- coding: utf-8 -*-


from sys import version_info as _version_info
from inspect import getmembers as _getmembers, isfunction as _isfunction, ismethod as _ismethod
from typing import Union, List
from datetime import datetime as _datetime
from numpy import empty as _empty, array as _array
from pyvacon.analytics import ptime as _ptime, CouponDescription as _CouponDescription, \
    vectorCouponDescription as _vectorCouponDescription, BaseObject as _BaseObject, \
    vectorVectorDouble as _vectorVectorDouble, vectorDouble as _vectorDouble


def create_ptime(date: Union[_datetime, _ptime]) -> _ptime:
    """ Converts dates from give datetime to ptime format. Leaves dates given in ptime format unchanged.

    Args:
        date (datetime, ptime): The input datetime/ptime which will be converted to ptime.

    Returns:
        _ptime: (converted) date
    """
    if type(date) is _ptime:
        return date
          
    if type(date) is _datetime:
        result = _ptime(date.year, date.month, date.day, date.hour, date.minute, date.second)
        return result


def _convert(x):
    if isinstance(x, _datetime):
        return create_ptime(x)
    if isinstance(x, list) and len(x) > 0:
        if isinstance(x[0], _datetime):
            return [create_ptime(y) for y in x]
        if isinstance(x[0], _CouponDescription):
            coupons = _vectorCouponDescription()
            for coupon in x: 
                coupons.append(coupon)
            return coupons
    return x


def converter(f):
    def wrapper(*args, **kwargs):
        new_args = [_convert(x) for x in args]
        result = f(*new_args, **kwargs)        
        return result
    return wrapper


def _get_dict_repr(obj):
    import json

    def cleanup_dict(d):
        if not isinstance(d, dict):
            return d
        if len(d) == 1:
            for v in d.values():
                return v
        new_dict = {}
        for item, value in d.items():
            if item != 'cereal_class_version' and item != 'polymorphic_id' and item != 'UID_':
                if isinstance(value, dict):
                    if len(value) == 1:
                        for v in value.values():
                            new_dict[item] = v
                    else:
                        new_dict[item] = cleanup_dict(value)
                elif isinstance(value, list):
                    new_dict[item] = [cleanup_dict(vv) for vv in value]
                else:
                    new_dict[item] = value
        return new_dict
        
    represent = str(_BaseObject.getString(obj)) + '}'
    d = json.loads(represent)
    return cleanup_dict(d['value0'])


def _get_string_rep(obj):
    d = _get_dict_repr(obj)
    return str(d)


if _version_info >= (3, 0, ):
    def _add_converter(cls):
        for attr, item in _getmembers(cls, _isfunction):  # for python 2 : ismethod
            setattr(cls, attr, converter(item))
        for name, method in _getmembers(cls, lambda o: isinstance(o, property)):
            setattr(cls, name, property(converter(method.fget), converter(method.fset)))
        setattr(cls, '__str__', _get_string_rep)
        setattr(cls, 'get_dictionary', _get_dict_repr)
        return cls
else:
    def _add_converter(cls):
        for attr, item in _getmembers(cls, _ismethod):  # for python 3 : isfunction
            setattr(cls, attr, converter(item))
        for name, method in _getmembers(cls, lambda o: isinstance(o, property)):
            setattr(cls, name, property(converter(method.fget), converter(method.fset)))
        setattr(cls, '__str__', _get_string_rep)
        setattr(cls, 'get_dictionary', _get_dict_repr)
        return cls

    
def create_datetime(date: _ptime) -> _datetime:
    """[summary]

    Args:
        date (ptime): [description]

    Returns:
        datetime: [description]
    """
    return _datetime(date.year(), date.month(), date.day(), date.hours(), date.minutes(), date.seconds())


def to_np_matrix(mat: _vectorVectorDouble) -> _array:
    """[summary]

    Args:
        mat (vectorVectorDouble): [description]

    Returns:
        array: [description]
    """
    if len(mat) == 0:
        return _empty([0, 0])
    result = _empty([len(mat), len(mat[0])])
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            result[i][j] = mat[i][j]
    return result


def from_np_matrix(mat: _array) -> _vectorVectorDouble:
    rows, cols = mat.shape
    result = _vectorVectorDouble(rows)
    for i in range(rows):
        tmp = _vectorDouble(cols)
        for j in range(cols):
            tmp[j] = mat[i][j]
        result[i] = tmp
    return result
