from functools import wraps
from io import TextIOWrapper, StringIO
from logging import Logger
import sys
import time
from typing import Callable, TextIO


def timeit(file: TextIO =sys.stdout, logger: Logger =None) -> Callable:
    def _timeit(func):
        @wraps(func)
        def _wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            msg = "{} ran in {:.3f}s with params {}, {}\n".format(
                func.__name__, round(end - start, 2), args, kwargs)

            if isinstance(file, TextIOWrapper) or isinstance(file, StringIO):
                file.writelines(msg)
                file.flush()

            if isinstance(logger, Logger):
                logger.info(msg)
            return result

        return _wrapper

    return _timeit
