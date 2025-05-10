str1= "this is my homepage"
len1= len(str1)
str2= "you are mine.\tand i am with you"
str3= "this is my python code.\nwe are creating it in python"
finalStr= str2+ " "+ str3
print (str3)
print (str2)
# print (finalStr)

#concatination
str4= "hello"
str5= "world"
print(str4+str5)



#length
print(len1)
str6 = "my college"
ch = str6[0]
print (ch)
ch1 = str6[4]
print (ch1)



# this process is called slicing
print (str6[0:2])
print (str6[3:10])
print (str6[4:8])
print (str6[3:len(str6)])


# using negetive index
strMain = "apple"
print (strMain[-3:-1])
print (strMain[-5:-1])
print (strMain[-5:])

#strings functions example


# using endswith
print (strMain.endswith("ple"))
print (strMain.endswith("app"))
# aikehne bojhacce j app te shesh hocce kina string ta, thik hole true ashbe ar na hoile false ashbe


# using capitalize
print(strMain.capitalize())

# using replace
print(strMain.replace("p", "r"))
print(strMain.replace("apple", "banana"))


# using find
print(strMain.find("e"))
# result a ar index value ta show korbe
print(strMain.find("h"))

# using count
print(strMain.count("p"))
