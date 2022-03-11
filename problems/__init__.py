import time
import logging


class TimeMethodMixin:
    @staticmethod
    def time_method(func, *args, **kwargs):
        t1 = time.perf_counter()

        response = None
        except_instance = None
        try:
            response = func(*args, **kwargs)
        except Exception as e:
            except_instance = e
        t2 = time.perf_counter()

        logging.info(f'Execution in {(t2 - t1)} seconds')

        if except_instance is not None:
            raise except_instance

        return response
