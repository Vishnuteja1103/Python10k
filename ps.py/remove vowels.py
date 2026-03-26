# .remove vowels in a string
str=input("enter a string:")
ans=""
for i in str:
    if i not in "aeiouAEIOU":
        ans+=i
print(ans)