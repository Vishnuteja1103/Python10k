sec=int(input("enter seconds: "))
hours=sec//3600
sec=sec%3600
min=sec//60
sec=sec%60
print(f"{hours}:{min}:{sec}")
