def outer(fun):
    def inner():
        arr=[1,2,3,4,5]
        b=-9999
        for i in arr:
            if i>b:
                b=i
        print(b)
    fun()
    return inner
@outer
def greet():
    print("bigger")

greet()
