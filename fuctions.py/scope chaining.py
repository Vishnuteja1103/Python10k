def outer():
    a=10
    b=20
    def inner():
        nonlocal a
        a+=30
        print(a+b)
    def sub():
        nonlocal b
        b-=49
        print(a-b)
    # print(inner,sub)
    inner(),sub()

outer()
# outer()[1]