def outer(fun):
    def inner():
        arr=[4,2,13,15,3,34]
        max=0
        secondmax=0
        for i in arr:
            if i > max:
                secondmax=max
                max=i
            elif i>secondmax and i<max:
                secondmax=i
        print(secondmax)
        fun()
    return inner
@outer
def info():
    print("secondmax")
info()
 