#Type of string text
# boundries

'string text' "string text" '''string text''' """string text"""
name : str = "Muhammad Zain"
fathername : str = "Muhammad"
education : str = "Photographer"
age : int = 18
card : str = "Student ID card\nStudent name:" 
print(card)

#Difine multiline string """abc""" , ''' abc '''  

studentname : str = "Muhammad Zain"
fathername : str = "Muhammad"
education : str = "Photographer"
age : int = 18

card : str = """Student ID card 
Student name =
fathername =
education =
age =
"""
print(card)

#using F-string 

studentname : str = "Muhammad Zain"
fathername : str = "Muhammad"
education : str = "Photographer"
age : int = 18

card : str = f"""Student ID card 
Student name ={studentname}
fathername ={fathername}
education ={education}
age ={age}
"""

#Using %s and %d 
#%d = Ye integer values (whole numbers) ke liye use hota hai.
#%s = Ye strings (text values) ke liye use hota hai. Yeh kisi bhi data type ko string mein convert kar sakta hai
studentname : str = "Muhammad Zain"
fathername : str = "Muhammad"
education : str = "Photographer"
age : int = 18

card : str = f"""Student ID card 
Student name=%s
fathername =%s
education =%s
age =%d
"""%(studentname,fathername,education,age)
print(card)

#for all methods of string
[i for i in dir(str) if"_" not in i]

#Using method
# code no 1
name : str = "MuHaMmAd ZaIn"
print(name.capitalize())

#.formate code no 1
a = 7
b = 8
#  {} place holder 
"Pakistan value a = {} and value b = {}".format(a,b)
 #code no 2 
name : str = "Muhammad Zain"
fname : str = "Muhammad"
education : str = "Photographer"
age : int = 18

card : str = """
Student ID card 
Student name : {a}
fathername : {b}
Education = {c}
Age ={d}

""".format(a=name, b=fname, c=education, d=age)
print(card)