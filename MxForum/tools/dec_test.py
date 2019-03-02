#装饰器是什么样的
#装饰器加载过程
import functools
import time

def time_dec(func):
    print("dec started")
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("last_time:{}".format(end_time - start_time))
    return wrapper

@time_dec
def add(a, b):
    time.sleep(3)
    return a+b


if __name__ == "__main__":
    #1. 为什么我们调用add的时候报错是wrapper
    #2. 变量如何传递到wrapper中
    print(add(1,2))