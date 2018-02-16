arr=[]
num=int(input("Enter num of elements:"))
print("\nEnter %d elements"%num)
for x in range(1, num+1):
	add=int(input())
	arr.append(add)
print("\nmaxinum element is: ",max(arr))
