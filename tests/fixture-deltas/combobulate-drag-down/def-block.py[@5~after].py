# -*- combobulate-test-point-overlays: ((1 outline 185) (2 outline 230) (3 outline 248) (4 outline 295) (5 outline 333)); eval: (combobulate-test-fixture-mode t); -*-


def foo():
    a = {1: 2, 3: 4}
    # some comment here
    b = (1, 2, 3)
    """
    This is a multiline string
    """
    some_func(1, 2, {"a": 1, "b": 2})
    return a, b
