#TO FIND FACTORIAL OF GIVEN NUMBER
num=int(input("Enter a number N: "))
res=0
if num>0:
	for x in range(1,num+1):
		res=res+x
		print (res)
else:
	print ("Enter a positive number")
