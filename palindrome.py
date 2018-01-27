num = input('Enter a number b/w 1 & 1000 : ')
if num<=1000:
	if num == str(num)[::-1]:
		print('yes')
	else:
        		print('no')
else:
	print("enter a valid number")
