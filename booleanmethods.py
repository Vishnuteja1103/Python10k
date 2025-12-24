#boolean methods 

#isupperr() it only checks upto characetr only
# s1="vishnu tinnavara"
# print(s1.isupper())
# s2="VISHNU123"
# print(s2.isupper())
# s3="VISHNU 123"
# print(s3.isupper())

#islower() it only checks upto characetr only
# s1="hellowold@123"
# print(s1.islower())
# s2="hello World"
# print(s2.islower())

#isspace() it checks wheather is string contain spaces only
# s1="hello world"
# print(s1.isspace())
# s2=" helloworld"
# print(s2.isspace())
# s3="  "
# print(s3.isspace())


# isalpha() it checks the string contain only alphabets or not 
# s1="hello world"
# print(s1.isalpha())
# s2="helloworld"
# print(s2.isalpha())
# s3="abc123"
# print(s3.isalpha())

# isdigit() it check the string only contain  only digits or not 
# s1="vishnu_x11"
# print(s1.isdigit())
# s2="12345678"
# print(s2.isdigit())
# s3="1234vishnu"
# print(s3.isdigit())

#startswith(prefix,si,ei)  it check the wheather the string start with particular character ot not (or) multi character 
# s1="hello vishnu teja korada"
# print(s1.startswith("h"))
# print(s1.startswith("hello"))
# print(s1.startswith("r"))
# print(s1.startswith("v",3))
# print(s1.startswith("v"))


##endswith(prefix,si,ei)  it check the wheather the string ends with particular character ot not (or) multi character 
# s1="hello world 123"
# print(s1.endswith("3"))
# print(s1.endswith(" 123"))
# print(s1.endswith("rld"))


#isalnum() it check the either alphabets and number or both num and alp

s1="hello 123"
print(s1.isalnum())
s2="hello"
print(s2.isalnum())
s3="1234"
print(s3.isalnum())
s4="vishnuuux11"
print(s4.isalnum())