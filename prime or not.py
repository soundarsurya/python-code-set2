num=int(input("Enter a number: "))
if num>1 and num<=1000:
	for x in range(2,num):
    	if num%x == 0:
      		print ("No")
	else:
    	print("Yes")
else:
	print("enter a valid number")
