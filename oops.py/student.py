class student:
    collagename="raghu"
    def __init__(self,name,branch,section,year):
        self.name=name
        self.branch=branch
        self.section=section
        self.year=year
    def method(self):
        print(self.collagename,self.name,self.branch,self.section,self.year,)
        # print(self.name)
        # print(self.branch)
        # print(self.section)
        # print(self.year) 
 
s1=student("vishnu","cse","b","2021")
s2=student("dinesh","cse","a",2021)
s3=student("charan","ece","c","2019")
s4=student("vamsi","meh","d","2021")
s5=student("ram","civil","e","2020")

s1.method()
s2.method()
s3.method()
s4.method()
s5.method()

