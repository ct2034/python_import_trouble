if __name__ != '__main__':
    from . import my_dep


def bar():
    return my_dep.foo() + 1


if __name__ == '__main__':
    import my_dep
    print(bar())
