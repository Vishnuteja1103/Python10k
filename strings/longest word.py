#find the longest word in a sentense?
s=input("enter a sentense:")
word=s.split()
longest=word[0]

for i in word:
    if len(i)>len(word):
        longest=i

print(longest)