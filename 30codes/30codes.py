# 1. Add an Element to a List
# Problem: Write a function to add an element to a list. 
# Explanation: Use append() to add the element to the end. Input: [1, 2, 3], add 4 Output: [1, 2, 3, 4]
l=[1,2,3]
l.append(4)
print(l)
# 2. Remove an Element from a List
# Problem: Write a function to remove a specific element from a list.
#  Explanation: Use remove() or pop() if index is known. Input: [1, 2, 3, 4], remove 3 Output: [1, 2, 4]
l1=[1,2,3,4]
l1.remove(3)
print(l1)
# 3. Find Maximum in ListProblem: Find the maximum value in a list.
#  Explanation: Use max() or iterate manually. Input: [4, 7, 1, 9] Output: 9
l2=[4,7,1,9]
print(max(l2))
# 4. Find Minimum in List Problem: Find the minimum value in a list.
#  Explanation: Use min() or iterate manually. Input: [4, 7, 1, 9] Output: 1
l3=[4,7,1,9]
print(min(l3))  
# 5. Sum of All Elements in List Problem:
#  Write a function to find the sum of all list elements.
#  Explanation: Use sum() or loop to add all items. Input: [1, 2, 3] Output: 6
l4=[1,2,3]
print(sum(l4))
# 6. Count Occurrence of an Element Problem:
#  Count how many times a value appears in a list.
#  Explanation: Use count() method. Input: [1, 2, 2, 3, 2], value 2 Output: 3
l5=[1,2,2,3,2]
print(l5.count(2))
# 7. Reverse a List Problem: Write a function to reverse the order of list elements.
#  Explanation: Use slicing or reverse() method. Input: [1, 2, 3] Output: [3, 2, 1]
l6=[1,2,3]
l6.reverse()
print(l6[::-1])
print(l6)
# 8. Sort a List Problem: Write a function to sort a list in ascending order. 
# Explanation: Use sort() or sorted(). Input: [4, 1, 3, 2] Output: [1, 2, 3, 4]
l7=[4,1,3,2]
l7.sort()
print(l7)
# 9. Remove Duplicates from a List Problem: Eliminate duplicate values.
#  Explanation: Use set() or manual loop. Input: [1, 2, 2, 3] Output: [1, 2, 3]
l8=[1,2,2,3]
l=[]
for i in l8:
    if i in l:
        pass
    else:
        l.append(i)
print(l)
# 10. Merge Two Lists Problem: Merge two lists into one. 
# Explanation: Use + operator or extend(). Input: [1, 2], [3, 4] Output: [1, 2, 3, 4]
l9=[1,2]
l10=[3,4]
print(19)
print(l9+l10)
# 11. Find Common Elements in Two Lists Problem:
#  Return common elements between two lists. Explanation: Use set() and & or loops.
#  Input: [1, 2, 3], [2, 3, 4] Output: [2, 3]
l11=[1,2,3]
l12=[2,3,4]
li=[]
for i in l11:
    if i in l12:
        li.append(i)
print(li)
# 12. Print Even Numbers in a List Problem:
#  Print only even numbers from a list. Explanation: Use modulo condition in a loop.
#  Input: [1, 2, 3, 4] Output: [2, 4]
l13=[1,2,3,4,5,6]
l14=[]
for i in l13:
    if i%2==0:
        l14.append(i)
print(l14)
# 13. Print Odd Numbers in a List Problem: Print only odd numbers from a list.
#  Input: [1, 2, 3, 4] Output: [1, 3]
l15=[1,2,3,4,5]
l16=[]
for i in l15:
    if i%2!=0:
        l16.append(i)
print(l16)
# 14. Check if List is Palindrome Problem: Check if the list reads the 
# same forwards and backwards. Input: [1, 2, 1] Output: True
l17=[1,2,1]
l18=(l17[::-1])
if l17==l18:
    print(True)
else:
    print(False)
# 15. Count Positive, Negative, Zero Problem: Count the number of positive,
#  negative and zero values in a list. Input: [0, -1, 2, -3, 4] 
# Output: Positive: 2, Negative: 2, Zero: 1
l19=[0,-1,2,-3,4]
positive=0
negative=0
zero=0
for i in l19:
    if i >0:
        positive+=1
    elif i<0:
        negative+=1
    else:
        zero+=1
print(f"positive:{positive},negative:{negative},zero:{zero}")
# 16. Find Second Largest Number in List Problem: Find the second highest value.
#  Input: [1, 3, 4, 5, 0] Output: 4
l20=[1,3,4,5,0]
largest=float("-inf")
second_largest=float("-inf")
for i in l20:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i!=largest:
        second_largest=i

print(second_largest)
# 17. Find Second Smallest Number in List Problem: Find the second lowest value.
#  Input: [5, 1, 4, 2, 3] Output: 2
l21=[5,1,4,2,3]
smallest=float("inf")
secondsmallest=float("inf")
for i in l21:
    if i < smallest:
        secondsmallest=smallest
        smallest=i
    elif i<secondsmallest and i !=smallest:
        secondsmallest=i

print(secondsmallest)
# 18. Copy List to Another List Problem: Copy the contents of one list to another. 
# Explanation: Use slicing or copy(). Input: [1, 2, 3] Output: [1, 2, 3]
l22=[1,2,3]
l23=l22.copy()
print(l23)
# 19. Print All Prime Numbers in List Problem: Print all prime numbers from a list.
#  Input: [1, 2, 3, 4, 5] Output: [2, 3, 5]
l24=[1,2,3,4,5]
l25=[]
for i in l24:
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count+=1
    if count==2:
        l25.append(i)
print(l25)
# 20. Replace All Zeroes with a Given Number Problem:
#  Replace every zero with a specific value (e.g., -1).
#  Input: [0, 2, 0, 4], replace with -1 Output: [-1, 2, -1, 4]
l26=[0,2,0,4]
l27=[]
for i in l26:
    if i ==0:
        l27.append(-1)
    elif i!=0:
        l27.append(i)
print(l27)
# 21. Check if All Elements Are Same Problem: 
# Check whether all elements in the list are identical. 
# Input: [5, 5, 5, 5] Output: True
l28=[5,5,5,5]
t=True
for i in l28:
    if i !=l28[0]:
        t=False
        break
print(t)
# 22. Find Frequency of All Elements Problem:
#  Return a dictionary with the frequency of each element.
#  Input: [1, 2, 2, 3, 1] Output: {1: 2, 2: 2, 3: 1}
l29=[1,2,2,3,1]
d={}
for i in l29:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)
# 23. Flatten a Nested List Problem:
#  Convert a nested list into a single list. 
# Input: [[1, 2], [3, 4]] Output: [1, 2, 3, 4]
l30=[[1,2],[3,4]]
print(l30[0]+l30[1])
# 24. Split a List into Even and Odd Lists Problem:
#  Separate even and odd numbers into different lists.
#  Input: [1, 2, 3, 4, 5] Output: Even: [2, 4], Odd: [1, 3, 5]
l31=[1,2,3,4,5]
even=[]
odd=[]
for i in l31:
    if i %2==0:
        even.append(i)
    elif i%2!=0:
        odd.append(i)
print(f"even:{even} odd:{odd}")
# 25. Find Pair of Elements with Given Sum Problem: 
# Find all pairs in the list whose sum equals a given value. 
# Input: [1, 2, 3, 4], sum = 5 Output: [(1, 4), (2, 3)]
l32=[1,2,3,4]
sum=5
pairs = []
for i in range(len(l32)):
    for j in range(i + 1, len(l32)):
        if l32[i] + l32[j] == sum:
            pairs.append((l32[i], l32[j]))
print(pairs)
# 26. Remove All Odd NumbersProblem: 
# Remove all odd numbers from the list. 
# Input: [1, 2, 3, 4, 5] Output: [2, 4]
l33=[1,2,3,4,5]
l34=[]
for i in l33:
    if i%2==0:
        l34.append(i)
print(l34)
# 27. Remove All Even Numbers Problem: 
# Remove all even numbers from the list.
#  Input: [1, 2, 3, 4, 5] Output: [1, 3, 5]
l35=[1,2,3,4,5]
l36=[]
for i in l35:
    if i%2!=0:
        l36.append(i)
print(l36)
# 28. Multiply All Elements by a Number Problem:
#  Multiply every element in the list by a fixed number.
#  Input: [1, 2, 3], multiply by 2 Output: [2, 4, 6]
l37=[1,2,3]
l38=[]
for i in l37:
    l38.append(i*2)
print(l38)
#  29. Find Difference Between Max and Min Problem:
#  Return the difference between the largest and smallest element.
#  Input: [4, 2, 7, 1] Output: 6
l39=[4,2,7,1]
print(max(l39)-min(l39))
# 30. Check if a List is Empty Problem:
#  Write a function that returns True if the list is empty, else False.
#  Input: [] Output: True
l40=[]
if len(l40)==0:
    print(True)
else:
    print(False)



        