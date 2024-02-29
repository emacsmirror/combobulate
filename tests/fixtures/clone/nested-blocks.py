# -*- combobulate-test-point-overlays: ((1 outline 155)); eval: (combobulate-test-fixture-mode t); -*-


def foo():
    with some_manager() as x:
        if x:
            for y in x:
                print(y)
        else:
            return x
        try:
            print(x)
        except:
            pass
        finally:
            print(x)
        async with some_async_manager() as y:
            print(y)
