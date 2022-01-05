import my_dep


def bar():
    return my_dep.foo() + 1


if __name__ == '__main__':
    print(bar())
