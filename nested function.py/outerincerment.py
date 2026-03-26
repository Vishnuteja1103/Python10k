def outer():
    def inner():
        nonlocal a 
        a = 10
    inner()
    a+=1
    print(a)
outer()
outer()