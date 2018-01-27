start=int(input("Enter start number: "))
end=int(input("Enter end number: "))
for x in range(start+1,end):
	for y in range(2,start,end):
		if num%y == 0:
			print (y)
	else:
    		print("Yes")
else:
print("enter a valid number")
