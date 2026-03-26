#find the smallest word in a sentense?
s=input("enter a sentense:")
word=s.split()
smallest=word[0]

for i in word:
    if len(i)<len(smallest):
        smallest=i

print(smallest)