start=int(input("Enter start number: "))
end=int(input("Enter end num: "))
if start and end <100000:
	for x in range(start+1,end):
		if x%2 ==0:
			print(x)
else:
	print("Enter a valid number")
