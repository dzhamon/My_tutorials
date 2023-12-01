def foo(a, b, c, d, e, r):
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(r)


def foo2(*test, **kwargs):
    c = kwargs.get('c')
    if c is not None:
        print(c)

# foo(1, 3, 2, 3, 4, 5, )
print("#####################")
danniye = ("1", 2, 3)
drugiye_danniye = {"c": 3, "e": 4, "r": 5}
# foo2(**drugiye_danniye)

def foo3(a=1):
    if a == 5:
        return True
    else:
        a += 1
        print(a)
        foo3(a)

foo3()
