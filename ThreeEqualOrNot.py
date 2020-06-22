# !/ThreeNumbersEqualOrNot/


print("\nEnter three numbers to compare them :")

a = int(input("Enter 1st number:\n"))

b = int(input("Enter 2nd number:\n"))

c = int(input("Enter 3rd number:\n"))

if (a > b) and (a > c):

	print("A is Greater")

elif (b > a) and (b > c):

	print("B is Greater")

elif a == b == c:

	print("All are Equal")

else:

	print("C is Greater")