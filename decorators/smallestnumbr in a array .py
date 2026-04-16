def outer(fun):
    def inner():
        arr=[1,2,3,4,5]
        s=9999
        for i in arr:
            if i<s:
                s=i
        print(s)
    fun()
    return inner
@outer
def greet():
    print("smaller")

greet()
