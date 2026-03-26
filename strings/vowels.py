string=input("enter a string:")
vowelcount=0
consonantscount=0
for i in string:
    if i in "aeiouAEIOU":
        vowelcount+=1
    elif i not in "aeiouAEIOU !@#$%^&*()_-+,./'[]\{|}:;<>?" :
        consonantscount+=1


print("vowel count:",vowelcount)
print("consonants count:",consonantscount)