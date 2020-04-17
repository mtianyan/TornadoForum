# 1. 什么是协程
# 1.回调过深造成代码很难维护
# 2.栈撕裂造成异常无法向上抛出
# 协程- 可以被暂停并切换到其他协程运行的函数
from tornado.gen import coroutine


def yield_test():
    yield 1
    yield 2
    yield 3


async def yield_test2():
    yield 1
    # yield 2
    # yield 3


my_yield = yield_test()
for item in my_yield:
    print(item)


async def main():
    result = await yield_test2()
    print(result)
    # result = await yield_test2()


async def main2():
    await yield_test()

if __name__ == "__main__":
    import tornado
    io_loop = tornado.ioloop.IOLoop.current()

    # run_sync方法可以在运行完某个协程之后停止事件循环
    io_loop.run_sync(main)