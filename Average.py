totalnonerroneous=0
countnonerroneous=0
mylist = [3,5,-7,2,-1,6]
print("list is with faulty data points ",mylist)
for item in mylist:
    if item >=0:
        totalnonerroneous +=item
        countnonerroneous +=1
        
averagenonerroneous = totalnonerroneous/countnonerroneous
 
print("average of nonerroneous data :",averagenonerroneous)
 
for counter in range(len(mylist)):
    if mylist[counter]<0:
        mylist[counter]=averagenonerroneous
