import pandas as pd
f1=pd.read_csv("C:/Users/vishn/Downloads/netflix_titles.csv")
# print(f1)                      # prints the all the file data in the ternimal 

# print(f1.isnull()) # prints all the null with "true " like it was checking the value is null or not if its null it was true 

# print(f1.isnull().sum())  # shows the how many null values are there in the enteir column 

# print(f1.head(5)) # prints/shows the (head) means from the starting 5 records 

# print(f1.tail(5))   # prints/shows the (tail) means from the last/end 5 records

# print(f1["type"])  #print/show the specifi colunm with "column name<key>"

# print(f1["show_id"])  #print/show the specifi colunm with "column name<key>"

#----------------------------------------

#handling null values 

#fillna = used to fill the empty/nan/null values 

# print(f1["date_added"].fillna(" unkown ")) # fill all the empty values with unkown in "specific column"

# print(f1.fillna("loading"))   #fill all the empty values in entier  data with "loading" 

# ffill = fill the null values with previous values in the null value 

# print(f1["date_added"].ffill())

# ffill = fill the null values with next values in the null value 

# print(f1["date_added"].bfill()) 


