N=int(input("Enter a number N: "))
array=input()
num_list=list(map(int,array.split(',')))
rev_list=list(reversed(num_list))
print (num_list, rev_list)
if num_list==rev_list:
	print ("Yes")
else:
	print ("No")
