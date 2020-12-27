from io import StringIO
import time

from snipwizard.decorators import timeit

def test_timeit():
    
    output = StringIO()
    @timeit(output)
    def sleep_func(wait):
        time.sleep(wait)

    sleep_func(2)
    out_recv = output.getvalue().strip()
    assert out_recv.startswith("sleep_func ran in")
    assert out_recv.endswith("params (2,), {}")
