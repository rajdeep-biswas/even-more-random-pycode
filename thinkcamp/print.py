a = int(input('enter a: '))
b = int(input('enter b: '))
choice = int(input('1. add\n2. subtract\n3. multiply\n4. divide\nenter choice: '))

if choice == 1:
	res = a + b
elif choice == 2:
	res = a - b
elif choice == 3:
	res = a * b
elif choice == 4:
	res = a / b
else:
	print('wrong choice')

print('result: ' + str(res))
