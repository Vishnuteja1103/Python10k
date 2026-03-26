class student:
    company="amazom" #static variables
    def __init__(self,name,department,emp_id,experence):#local variables
        self.name=name                 #instance variable
        self.department=department      #instance variable
        self.emp_id=emp_id              #instance variable
        self.experence=experence            #instance variable
    def method(self):
        print(self.company,self.name,self.department,self.emp_id,self.experence,)
        # print(self.name)
        # print(self.branch)
        # print(self.section)
        # print(self.year)
 
s1=student("vishnu","HR","111103","4+")
s2=student("dinesh","floor manager","11","2+")
s3=student("charan","team_lead","45","5+")
s4=student("vamsi","manager","4512365","2+")
s5=student("ram","social media head","9874532","7+")

s1.method()
s2.method()
s3.method()
s4.method()
s5.method()

