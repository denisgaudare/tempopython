from line_profiler import profile
from loguru import logger


@profile
def my_function(x, y, z):
    # An error? It's caught anyway!
    return 1 / (x + y + z)
    time.sleep(5)



my_function(0,0,1)