count = 1
while count<=5 :
    print("hello")
    count +=1
    print(count)
    # 5 count true  na howa ponto aikahne condition cheak korte thakbe and true hoye gele lop stop hoye jabe
    # count is called iterator
    # in this whole procedure is called iteration

    i= 1
    while i<=10:
        print("my college",i)
        i +=1
        #print(i)

    i = 5
    while i >= 1:
        print(i)
        i -= 1
        print("loop ended")
        #print nuumbrs 1-100
    i = 1
    while i <= 100:
        print(i)
        i += 1
        #print("loop ended")


        # print numbers 100-1
    # i = 100
    # while i >= 1:
    #     print(i)
    #     i -= 1
    #     #print the multipication munber of table n
    #     n=int(input("enter the number:"))
    #     i = 1
    #     while i <= 10:
    #         print( n*i)
    #         i += 1

    # print the index of the list
list = ["superman", "thor", "ironman", "batman"]
# print(len(list))
idx = 0
while idx < len(list):
        print(list[idx])
        idx +=1

# break and continue
i = 0
while i <= 5:
    if i == 3:
        i += 1          # move past 3
        continue        # skip the rest of the loop body
    print(i)            # print when i is not 3
    i += 1              # increment every turn


# if i == 3:
# যদি বর্তমান i ঠিক ৩ হয়, তখন নিচের তিনটি ধাপ ঘটবে—
#
# i += 1 → i এক বাড়িয়ে ৪ করা হয়।
#
# continue → এই লাইনের কারণে লুপ-বডির বাকি অংশ (নীচের print ও i += 1) এ iteration-এ আর চলবে না। সরাসরি লুপের শুরুতে ফিরে যায়।
#
# ফলে ৩ কখনও প্রিন্ট হয় না; লুপ পরের মান ৪ থেকে চালু থাকে।

# for loop example
vegitables = [ "potato", "cucumber","ladyfinger","brockoli"]
for val in vegitables:
    print(val)

list = [12,34,44,2,33,234,34]
for val in list :
    print(val)