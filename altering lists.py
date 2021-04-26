mylist = [3,5,-7,2,-1,6]
print("original list",mylist)
index = 0
for item in mylist:
    if mylist[index]<0:
        mylist[index]= "no negative values"
    index += 1
    
print("altered list",mylist)
