# random
import random as r
print(r.random())#prints the random output from 0.0 to 0.1

# randint

print(r.randint(9,10))#prints the random output from range ( a,b)

# shuffle

anime=["one piece","naruto","hunterxhunter","MHA"]
r.shuffle(anime)#prints the values by randomly shuffling 
print(anime)

# choice

print(r.choice(anime))# prints the random single value from the input 


# choices

print(r.choices(anime,k=2))