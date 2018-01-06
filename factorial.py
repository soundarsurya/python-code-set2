#TO FIND FACTORIAL OF GIVEN NUMBER
num=int(input("Enter a number to find factorial: "))
res=1
if num>0:
	for x in range(1,num+1):
		 res=res*x
	print (res)
else:
	print ("Enter a positive number")
