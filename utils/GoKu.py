#!/usr/bin/env python
# coding:utf-8

import cProfile
import pstats
import time

from functools import wraps

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def temporary_cache(func):
    """Create cache area for recursive function.
    :param func: function name for function that will be decorated.
    :return: recursive value stored in the cache area if it exists in the cache area,
             recursive value calculates by the recursive function if not.
    :raise: None
    """
    cache = {}
    not_exist = object()

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = cache.get(args, not_exist)
        if result is not_exist:
            result = func(*args, **kwargs)
            cache[args] = result
        return result

    return wrapper


def profiler(func):
    """Analyze code performance, and give the analytical result.
    :param func: function name for function that will be decorated.
    :return: None
    :raise: None
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        prof = cProfile.Profile()
        prof.runcall(func, *args, **kwargs)
        stream = StringIO()
        ps = pstats.Stats(prof, stream=stream)
        ps.strip_dirs().sort_stats("cumulative").print_stats()
        print(stream.getvalue())

    return wrapper


def timer(func):
    """Get the time interval that executing the func.
    :param func: function name for function that will be decorated.
    :return: the result that the func return
    :raise: None
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Executing the {} used {:.3f}s.".format(func.__name__, end - start))
        return result

    return wrapper


def singleton(cls):
    """Define a class with a singleton instance.
    :param cls: class name for class that will be decorated.
    :return: isinstance for the cls class
    :raise: None
    """
    instances = {}

    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper
