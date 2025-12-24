#count()
# s1="hello world"
# print(s1.count("l"))
# print(s1.count("l",4,6))
# s2="jai maheshmathi"
# print(s2.count("m"))
# print(s2.count("a",3))
# print(s2.count("i"))

# split (separator,maxsplit)

# s1="hello world"
# s2=s1.split()
# print(s2)

# s1="malayalam"
# print(s1)
# print(s1.split("l"))

# s3="monkey d luffy"
# print(s3)
# print(s3.split())

# s4="hi python world"
# s1=s4.split("o")
# print(s1)
# s2=s4.split("i")
# print(s2)
# s3=s4.split("h")
# print(s3)

#rsplit(separator,maxsplit)
# s1="python world"
# s2=s1.rsplit()
# print(s2)

# s1="python world"
# s2=s1.rsplit("o",1)
# s3=s1.split("o",1)
# print(s2)
# print(s3)

#join()
#syntax:"separator".join(iterable)

# s1="hello world"
# s2="-".join(s1)
# print(s2)
# s3="3".join(s1)
# print(s3)

# s1="hello world" #output=hello-world
# s2=s1.split()
# s3="-".join(s2)
# print(s3)

# s2="who is riya " # output : ohw si ayir
# s1=s2.split()
# s3=s1[::-1]
# s4=" ".join(s3)
# s5=s4[::-1]
# print(s5)
# print(" ".join(s2[::-1].split()[::-1]))

# s1="hello python" #output:olleh nohtyp
# s2=s1.split()
# s3=s2[::-1]
# s4=" ".join(s3)
# s5=s4[::-1]
# print(s5)

#replace()
# s1="malayalam"
# s2=s1.replace("a","@")
# print(s2)

# s1="hello python world"
# s2=s1.replace(" ","-",1)
# s3=s2.split()
# s4="_".join(s3)
# print(s4)

s1="evvara meeratha cheppandra"
s2=s1.split()
s3=s2[::-1]
s4=" ".join(s3)
s5=s4[::-1]
s6=s5.replace(" ","@",1)
s7=s6.replace(" ","_",1)
print(s7)

