# list example
# marks = 23
# marks= 56
# marks = 67
# marks =235
marks = [45,67,98,43,789,8653]
print(marks)

print(type(marks))
all=["monika", 67, 78.9, "rashi"]
print(all)
print(all[1:3])
print(all[0:3])




# list method

num= [3,2,1]
print(num.append(4))
print(num)


print(list.sort(num))
print(num)


# sort to decending order
print(num.sort(reverse=True))
print(num)




# sort to acending order
print(num.reverse())
print(num)

list4 = ['ritu', 'rinty','rafa', 'asha']
print(list4.reverse())
print(list4)


list9= [1,3,4,6,78,9]
print(list9.insert(3,56))
print(list9)

print(list9.remove(3))
print(list9)
print(list9.pop(3))
print(list9)

# example
list8= []
print(list8)
print(list8.append("dobara"))
print(list8.append("thappad"))
print(list8.append("pink"))
print(list8)


movies =[]
# movies.append(input("enter your first movie:"))
# movies.append(input("enter your second movie:"))
# movies.append(input("enter your third movie:"))
mov1=(input("enter your first movie:"))
mov2=(input("enter your second movie:"))
mov3=(input("enter your third movie:"))

(movies.append(mov1))
(movies.append(mov2))
(movies.append(mov3))
print(movies)


#example of palindrome
#palinfrome is that which is -->which is same to look forward and backword
listMain= [1,2,1]
listMov= [1,2,3]
Main=listMain.copy()
Main.reverse()
if(Main==listMain):
    print("palindrome")
else:
    print(" not palindrome")



